for f in *.tex; do
  out="${f%.tex}.md"
  nkf -w "$f" | pandoc -f latex -t markdown -o "$out"
done
