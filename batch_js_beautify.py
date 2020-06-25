import shutil
import jsbeautifier
import toolkit_file

js_dir = r''


def beautify_js(file, inplace=True):
	print('Format: ' + file)
	fileFormatted = file + '.formatted'
	res = jsbeautifier.beautify_file(file)
	with open(fileFormatted, 'w', encoding='utf-8') as f:
		f.write(res)
	if inplace:
		shutil.move(fileFormatted, file)


if __name__ == '__main__':
    jsFileList = [x for x in toolkit_file.get_file_list(js_dir) if x.endswith('.js')]
    for file in jsFileList:
    	beautify_js(file)
    
