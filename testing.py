def _get_part_text(text:str,start:int,size:int) -> tuple[int,str]:
    text_part=text[start:start+size]
    end_corrector=re.stext_part