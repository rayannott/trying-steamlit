import streamlit as st


def create_list(lines, TAB='\t') -> list[str]:
    def count_tabs(s):
        i = 0
        cnt = 0
        while True:
            if s[i] == TAB:
                cnt += 1
                i += 1
            else:
                return cnt
    
    def get_numbering(level):
        res = []
        for lvl in range(level+1):
            res.append(str(levels_count[lvl]))
        return '.'.join(res) + '.'
    
    res = []
    levels = [count_tabs(line) for line in lines]
    levels_count = {lvl: 1 for lvl in range(max(levels)+1)}
    increase = set()
    prev_level = 0
    for line, level in zip(lines, levels):
        if level in increase:
            levels_count[level] += 1
            increase.remove(level)
        if prev_level < level:
            levels_count[level] = 1
        increase.add(level)
        res.append(f'{TAB*level}{get_numbering(level)} {line[level:]}')
        prev_level = level
    return res


TITLE = "Tab Text Enumeration"
st.set_page_config(page_title=TITLE, page_icon="📈")
st.markdown("# " + TITLE)
st.sidebar.header(TITLE)
st.write(
    """Here you can get ..."""
)

st.markdown('_Here will be a text_area widget_')
# input_txt = st.text_input('Text to transform')
# output_txt = st.text_area('', str(input_txt))
