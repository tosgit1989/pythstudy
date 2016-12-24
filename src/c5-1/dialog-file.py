import tkinter.filedialog as fd

path = fd.askopenfilename(
  title = "処理対象のファイルを選択してください",
  filetypes = [('HTML', '.html')]
)
print(path)