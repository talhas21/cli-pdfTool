import argparse
import sys
from rich.console import Console
from rich.theme import Theme
from pdf_merger import PdfMerger

# Define a custom theme for consistent terminal colors
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "bold yellow",
    "error": "bold red",
    "success": "bold green"
})
console = Console(theme=custom_theme)

def merge_command(args):
    console.print("[info]Initializing PDF Merger...[/info]")
    
    # Use output flag if provided, otherwise default to "merged.pdf"
    output_name = args.output if args.output else "merged.pdf"
    
    try:
        merger = PdfMerger(args.pdfs, output_name)
        
        # rich.status creates an animated spinner while process() runs
        with console.status(f"[warning]Merging {len(args.pdfs)} files into '{output_name}'...[/warning]", spinner="dots"):
            merger.process()
            
        console.print(f"[success]Merge complete![/success] [info]Output saved to {output_name}[/info]")
        
    except FileNotFoundError as e:
        console.print(f"\n[error]Termination Error:[/error] {e}")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[error]Unexpected Error:[/error] {e}")
        sys.exit(1)
    finally:
        console.print("[info]Process terminated.[/info]")

def main():
    parser = argparse.ArgumentParser(description="A CLI tool for PDF operations.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Command: merge
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs into one.")
    merge_parser.add_argument("pdfs", nargs="+", help="Space-separated list of PDF files to merge")
    merge_parser.add_argument("-o", "--output", help="Optional output filename (default: merged.pdf)")

    # Command: cut (Placeholder)
    cut_parser = subparsers.add_parser("cut", help="Cut/Split a PDF (Not yet implemented)")

    args = parser.parse_args()

    if args.command == "merge":
        merge_command(args)
    elif args.command == "cut":
        console.print("[warning]The 'cut' command is currently under construction.[/warning]")

if __name__ == "__main__":
    main()