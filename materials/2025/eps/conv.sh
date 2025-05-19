for f in *.eps; do
  gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha \
     -r300 -sOutputFile="${f%.eps}.png" "$f"
done
