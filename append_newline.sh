filename='append_newline.txt'
#read -p "Enter the text that you want to append:" newtext

#if [ "$newtext" != "" ]; then
      # Append the text by using '>>' symbol
echo "newtext\n" >> $filename
#fi
