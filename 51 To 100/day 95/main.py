# day 95 main File
# text finding same a mirror bot replace ect....
import re

pattern = "unified"
text = """Brother Jonathan is an 1825 historical novel about the American Revolution. Author John Neal (pictured) was considered one of America's top novelists at the time. The story explores cross-cultural relationships and highlights cultural diversity within the Thirteen Colonies, stressing egalitarianism and challenging the conception of a unified American nation. The book's sexual themes were explicit for the period, addressing female sexual virtue and male guilt for sexual misdeeds. Scholars praised Brother Jonathan's extensive and early use of realism in depicting American culture and speech. It is Neal's longest work and possibly the longest single work of American fiction until well into the"""

math = re.search(pattern,text)
print(math)