import zipfile
import xml.etree.ElementTree as ET

def get_strike_through_text(file_path, sheet_name, cell_address):
    # xlsxファイルをzipファイルとして開く
    with zipfile.ZipFile(file_path, 'r') as z:
        # ワークブックのリレーションシップを取得
        workbook_xml = z.read('xl/workbook.xml')
        workbook_root = ET.fromstring(workbook_xml)
        
        # シート名からシートIDを取得
        sheet_id = None
        for sheet in workbook_root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet'):
            if sheet.attrib['name'] == sheet_name:
                sheet_id = sheet.attrib['r:id']
                break

        # シートのリレーションシップを取得
        workbook_rels_xml = z.read('xl/_rels/workbook.xml.rels')
        workbook_rels_root = ET.fromstring(workbook_rels_xml)
        sheet_file = None
        for rel in workbook_rels_root.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            if rel.attrib['Id'] == sheet_id:
                sheet_file = rel.attrib['Target']
                break

        if sheet_file.startswith('/'):
            sheet_file = sheet_file[1:]

        # 対象のシートのxmlを取得
        sheet_xml = z.read(f'xl/{sheet_file}')
        root = ET.fromstring(sheet_xml)

        # セルのアドレスを指定して対象のセルを検索
        cell_ref = f'{cell_address[0]}{int(cell_address[1:])}'
        strike_through_text = []
        for row in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            for c in row:
                if c.attrib.get('r') == cell_ref:
                    # セルのリッチテキストを取得
                    for r in c.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}r'):
                        text_element = r.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                        if text_element is not None:
                            text = text_element.text
                            # 取消線のスタイルを確認
                            if r.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}rPr/{http://schemas.openxmlformats.org/spreadsheetml/2006/main}strike') is not None:
                                strike_through_text.append((text, True))
                            else:
                                strike_through_text.append((text, False))
        return strike_through_text

# 使用例
file_path = 'example.xlsx'
sheet_name = 'Sheet1'
cell_address = 'A1'

strike_text = get_strike_through_text(file_path, sheet_name, cell_address)
for text, is_strike in strike_text:
    if is_strike:
        print(f"取消線が設定されている文字: {text}")
    else:
        print(f"取消線が設定されていない文字: {text}")