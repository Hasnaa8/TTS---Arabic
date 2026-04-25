import pyarabic.araby as araby
import fileinput as fi
import sys
import mishkal.tashkeel

ALEF = 'ألف' 
BEH = 'باء'
TEH = 'تاء'
TEH_MARBUTA = 'تاء مربوطة'
THEH = 'ثاء'
JEEM = 'جيم'
HAH = 'حاء'
KHAH = 'خاء'
DAL = 'دال'
THAL = 'ذال'
REH = 'راء'
ZAIN = 'زاي'
SEEN = 'سين'
SHEEN = 'شين'
SAD = 'صاد'
DAD = 'ضاد'
TAH = 'طاء'
ZAH = 'ظاء'
AIN = 'عين'
GHAIN = 'غين'
FEH = 'فاء'
QAF = 'قاف'
KAF = 'كاف'
LAM = 'لام'
MEEM = 'ميم'
NOON = 'نون'
HEH = 'هاء'
WAW = 'واو'
YEH = 'ياء'
HAMZA = 'همزة'
ALEF_MADDA = 'ألف ممدودة'
ALEF_MAKSURA = 'ألف مقصورة'
ALEF_HAMZA_ABOVE = 'همزة على الألف'
WAW_HAMZA = 'همزة على الواو'
ALEF_HAMZA_BELOW = 'همزة تحت الألف'
YEH_HAMZA = 'همزة على الياء'
FATHATAN = 'فتحتان'
DAMMATAN = 'ضمتان'
KASRATAN = 'كسرتان'
FATHA = 'فتحة'
DAMMA = 'ضمة'
KASRA = 'كسرة'
SHADDA = 'شدة'
SUKUN = 'سكون'

harf = {\
    ALEF: u"ا", \
    BEH: u"ب", \
    TEH: u'ت', \
    TEH_MARBUTA: u'ة', \
    THEH: u'ث', \
    JEEM: u'ج', \
    HAH: u'ح', \
    KHAH: u'خ', \
    DAL: u'د', \
    THAL: u'ذ', \
    REH: u'ر', \
    ZAIN: u'ز', \
    SEEN: u'س', \
    SHEEN: u'ش', \
    SAD: u'ص', \
    DAD: u'ض', \
    TAH: u'ط', \
    ZAH: u'ظ', \
    AIN: u'ع', \
    GHAIN: u'غ', \
    FEH: u'ف', \
    QAF: u'ق', \
    KAF: u'ك', \
    LAM: u'ل', \
    MEEM: u'م', \
    NOON: u'ن', \
    HEH: u'ه', \
    WAW: u'و', \
    YEH: u'ي', \
    HAMZA: u'ء', \
    ALEF_MADDA: u'آ', \
    ALEF_MAKSURA: u'ى', \
    ALEF_HAMZA_ABOVE: u'أ', \
    WAW_HAMZA: u'ؤ', \
    ALEF_HAMZA_BELOW: u'إ', \
    YEH_HAMZA: u'ئ', \
    FATHATAN: u'_ً', \
    DAMMATAN: u'_ٌ', \
    KASRATAN: u'_ٍ', \
    FATHA: u'_َ', \
    DAMMA: u'_ُ', \
    KASRA: u'_ِ', \
    SHADDA: u'_ّ', \
    SUKUN: u'_ْ', \
}

mapp = {\
    u'ا' : "a", \
    u'ب' : "b", \
    u'ت': "t", \
    u'ث': "T", \
    u'ج': "Z", \
    u'ح': "X", \
    u'خ': "x", \
    u'د': "d", \
    u'ذ': "D", \
    u'ر': "r", \
    u'ز': "z", \
    u'س': "s", \
    u'ش': "S", \
    u'ص': "s.", \
    u'ض': "d.", \
    u'ط': "t.", \
    u'ظ': "z.", \
    u'ع': "H", \
    u'غ': "G", \
    u'ف': "f", \
    u'ق': "q", \
    u'ك': "k", \
    u'ل': "l", \
    u'م': "m", \
    u'ن': "n", \
    u'ه': "h", \
    u'و': "w", \
    u'ي': "j", \
    u'ء': "?", \
    u'_َ': "a", \
    u'_ُ': "u", \
    u'_ِ': "i", \
    ' ' : "_", \
    '.' : "_", \
    '،' : "_", \
}

sun = ['ت', 'ث', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض' \
           , 'ط', 'ظ', 'ل', 'ن']
moon = ['ء', 'ا', 'ب', 'ج', 'ح', 'خ', 'ع', 'غ', 'ف', 'ق', 'ك', 'م', 'ه', 'و', 'ي']

# long
one = ['_َ', '_ُ', '_ِ', 'ء']
two= ['ب', 'ت' ,'د', 'ق', 'ك', 'ط' ,'ض', 'ظ']
three = ['ج', 'ذ' , 'ر']
four = [ 'غ', 'ل', 'ه', 'ث','ع', 'ز']
six = ['ا', 'و', 'ي']

def set_indexes_noqta(x):
    indexes = []
    for i in range(0, len(x)):
        if x[i] =='.':
            indexes.append(i)
    if not indexes:
        indexes.append(len(x))
    return indexes

def bs(i, ind):
    low = 0
    high = len(ind) - 1
    res = -1  

    while low <= high:
        mid = (low + high) // 2
        
       
        if ind[mid] > i:
            res = mid
            high = mid - 1  
        
        else:
            low = mid + 1
    # إذا فشل البحث، أرجع آخر عنصر موجود في القائمة (النهاية)
    if res == -1:
        return len(ind) - 1
    return res

def set_duration_and_pitch(x, ind):
    data = []
    base_pitch = 150
    range_pitch = 0.5
    pitch = base_pitch
    # تأكد من أن ind ليست فارغة لتجنب IndexError
    if not ind:
        ind = [len(x)]
    end = ind[bs(0, ind)]
        
    for i in range(0, len(x)):
        char = x[i]
        progress = i / (end - i) if end - i > 1 else 0 
        pitch = base_pitch
        pitch = pitch - range_pitch*progress
           
        if char in [' ']:
            continue
        elif char in ['،']:
            #progress = i/(bs(i,x)) if bs(i,x) > 1 else 0
            pitch += 5 
            data.append((char, 35, pitch, pitch - range_pitch*progress))
        elif char in '.':
            end = ind[bs(i, ind)]
            progress = i / (end - i) if end - i > 1 else 0    
            pitch -= 10
            data.append((char, 45, pitch, pitch - range_pitch*progress))   
        elif char in six:
            if i + 1 < len(x) and x[i+1] == harf['شدة']:
                data.append((char, 300, pitch, pitch - range_pitch*progress))
            else:
                data.append((char, 150, pitch, pitch - range_pitch*progress))
        elif char in one:
            data.append((char, 75, pitch, pitch - range_pitch*progress))
        elif char in three:
            if i + 1 < len(x) and x[i+1] == harf['شدة']:
                data.append((char, 200, pitch, pitch - range_pitch*progress))
            else:
                data.append((char, 100, pitch, pitch - range_pitch*progress))
        elif char in two:
            if i + 1 < len(x) and x[i+1] == harf['شدة']:
                data.append((char, 180, pitch, pitch - range_pitch*progress))
            else:
                data.append((char, 90, pitch, pitch - range_pitch*progress))
        elif char in four:
            if i + 1 < len(x) and x[i+1] == harf['شدة']:
                data.append((char, 230, pitch, pitch - range_pitch*progress))
            else:
                data.append((char, 115, pitch, pitch - range_pitch*progress))
        elif char not in ['_ْ', harf[SHADDA]]:
            if i + 1 < len(x) and x[i+1] == harf['شدة']:
                data.append((char, 260, pitch, pitch - range_pitch*progress))
            else:
                data.append((char, 130, pitch, pitch - range_pitch*progress))
        elif char not in harf[SHADDA]:
            data.append((char, 0, pitch, pitch - range_pitch*progress))
    data.append((' ', 45, pitch, pitch - range_pitch*progress))
    data.append((' ', 45, pitch, pitch - range_pitch*progress)) 
    return data


def convert_to_phoneme(data):
    phoneme = []
    for i in range(0,len(data)):
        
        if not data[i][0] or data[i][0] not in mapp:
            # print(data[i][0])
            continue
        
        if data[i][1] == 0:
            continue
        elif data[i][0] not in ["_ِ", "_ُ", "_َ"]:
            if mapp[data[i][0]] in ["?"] and i + 1 < len(data) and mapp[data[i+1][0]] in ["a", "u", "i"]:
                continue
            else:
                if i + 1 < len(data) and data[i+1][1] == 0:
                    phoneme.append((mapp[data[i][0]], data[i][1] + 0.09 * data[i][1], data[i][2], data[i][3]))
                elif mapp[data[i][0]] == "a" and i - 1 >= 0 and mapp[data[i-1][0]] in ["s.","d.", "t." , "z."]:
                    phoneme.append(("a.", data[i][1], data[i][2], data[i][3]))
                else:
                    phoneme.append((mapp[data[i][0]], data[i][1], data[i][2], data[i][3]))
        else:
            if mapp[data[i-1][0]] in ["s.", "d.", "t.", "z."]:
                if mapp[data[i][0]] in ["a"]:
                    phoneme.append(("a.", data[i][1], data[i][2], data[i][3]))
                elif mapp[data[i][0]] in ["u"]:
                    phoneme.append(("u.", data[i][1], data[i][2], data[i][3]))
                else:
                    phoneme.append(("i.", data[i][1], data[i][2], data[i][3]))
            else:
                phoneme.append((mapp[data[i][0]], data[i][1], data[i][2], data[i][3]))
    return phoneme


def convert_to_phofile(phoneme):
    with open("output_file.pho" , "w", encoding = "utf-8") as f:
        for p in phoneme:
            f.write(f"{p[0]} {p[1]} {p[2]} {p[3]}\n")
        # print(f"{output_file}")
#  ال التعريف + الف التفريق+ شدات + ننوين
def al_alta3reef_and_alef_altafreeq_and_shadda_and_tanween(x):
    i = 0
    ans = []

    for j in range(0, len(x)):
        if i == len(x):
            break
        if x[i] == harf[LAM] and i + 1 < len(x) and x[i+1] == harf[SHADDA] and i + 2 < len(x) and x[i+2] == harf[FATHA] and i + 3 < len(x) and x[i+3] == harf[HEH]:
            if i - 1 >= 0 and x[i-1] == harf[KASRA] and i - 2 >= 0 and x[i-2] == harf[LAM] and  (i - 3  >= 0 and x[i-3] == ' ' or i - 3 < 0 ) :
                ans.append(harf[LAM])

                ans.append(harf[SHADDA])
                ans.append(harf[ALEF])
                i = i + 2
            elif i - 1 >= 0 and x[i-1] == harf[LAM] and (i - 2  >= 0 and x[i-2] == harf[ALEF] and i - 3 >= 0 and x[i-3] == ' '):
                ans.append(harf[LAM])
           
                ans.append(harf[SHADDA])
                ans.append(harf[ALEF])
                i = i + 2
                                                      
        elif i - 1 >= 0 and x[i-1] == " " and x[i] == harf['ألف'] and i + 1 < len(x) and x[i+1] == harf['لام'] and i + 2 < len(x) and x[i+2] in sun:
            i = i + 1
        elif i - 1 >= 0 and x[i-1] == " " and x[i] == harf['ألف'] and i + 1 < len(x) and x[i+1] == harf['لام'] and i + 2 < len(x) and x[i+2] in moon:
            print('*')
            ans.append(harf['لام'])
            ans.append(harf['سكون'])
            i = i + 1
        elif ((i == 0) or (i - 1 >= 0 and x[i-1] == " " and i - 2 >=0 and x[i-2] in ['.', '،'])) and x[i] == harf['ألف'] and i + 1 < len(x) and x[i+1] == harf['لام'] and i + 2 < len(x) and x[i+2] in sun:
            # shamsya
            ans.append(harf['همزة'])
            ans.append(harf['فتحة'])
            i = i + 1
        elif ((i == 0) or (i - 1 >= 0 and x[i-1] == " " and i - 2 >=0 and x[i-2] in ['.', '،'])) and x[i] == harf['ألف'] and i + 1 < len(x) and x[i+1] == harf['لام'] and i + 2 < len(x) and x[i+2] in moon:
            ans.append(harf['همزة'])
            ans.append(harf['فتحة'])
            ans.append(harf['لام'])
            ans.append(harf['سكون'])
            i = i + 1
        elif x[i] == harf['ألف'] and i - 1 >= 0 and x[i-1] == harf['واو'] and (i == len(x) - 1 or (i + 1 < len(x) and x[i+1] in ['.', '،', ' '])):
            pass
        elif (i - 1 >= 0 and x[i-1] == " " and (i - 2 >= 0 and x[i-2] == harf['ألف']) or i == 0) and x[i] == harf['ألف']:
            # print('*')
            pass
        elif (i - 1 >= 0 and x[i-1] == " "  or i == 0) and x[i] == harf['ألف']:
            print('*')
            ans.append(harf['كسرة'])
        elif x[i] == harf['شدة']:
            ans.append(x[i])
            if i + 2 < len(x):
                if x[i+1] == harf['ضمة'] and x[i+2] == harf['واو'] or x[i+1] == harf['كسرة'] and x[i+2] == harf['ياء'] or x[i+1] == harf['فتحة'] and x[i+2] == harf['ألف']:
                    i = i + 1
                    pass
                elif x[i+1] in [harf['فتحة'], harf['ضمة'], harf['كسرة'] ,harf['فتحتان'], harf['كسرتان'], harf['ضمتان']]:
                    if x[i] == harf['فتحتان']:
                        ans.append(harf['فتحة'])
                        ans.append(harf['نون'])
                        ans.append(harf['سكون'])
                    elif x[i] == harf['ضمتان']:
                        ans.append(harf['ضمة'])
                        ans.append(harf['نون'])
                        ans.append(harf['سكون'])
                    elif x[i] == harf['كسرتان']:
                        ans.append(harf['كسرة'])
                        ans.append(harf['نون'])
                        ans.append(harf['سكون'])
                        
                else:
                    ans.append(x[i+1])
                    i = i + 1
        elif x[i] in [harf['فتحة'], harf['ضمة'], harf['كسرة'] ,harf['فتحتان'], harf['كسرتان'], harf['ضمتان']]:
            if i == len(x) - 1 or (i + 1 < len(x) and x[i+1] == '.'):
                if x[i] == harf['فتحتان'] and x[i-1] == harf['ألف']:
                    ans.pop()
                    ans.append(harf['فتحة'])
                    ans.append(harf['نون'])
                    ans.append(harf['سكون'])

                pass
            else:
                if x[i] == harf['فتحتان']:
                    if x[i-1] == harf['ألف']:
                        ans.pop()
                        ans.append(harf['فتحة'])
                        ans.append(harf['نون'])
                        ans.append(harf['سكون'])
                    else:
                        ans.append(harf['فتحة'])
                        ans.append(harf['نون'])
                        ans.append(harf['سكون'])
                elif x[i] == harf['ضمتان']:
                    ans.append(harf['ضمة'])
                    ans.append(harf['نون'])
                    ans.append(harf['سكون'])
                elif x[i] == harf['كسرتان']:
                    ans.append(harf['كسرة'])
                    ans.append(harf['نون'])
                    ans.append(harf['سكون'])
                else:
                    if x[i] == harf['فتحة'] and i + 1 < len(x) and x[i+1] == harf['ألف']:
                        pass
                    elif x[i] == harf['ضمة'] and i + 1 < len(x) and x[i+1] == harf['واو']:
                        pass
                    elif x[i] == harf['كسرة'] and i + 1 < len(x) and x[i+1] == harf['ياء']:
                        pass
                    else :
                        ans.append(x[i])
        elif x[i] == harf['واو'] and i - 1 >= 0 and x[i-1] == harf['راء'] and i - 2 >= 0 and x[i-2] == harf['ميم'] and i - 3 >= 0 and x[i-3] == harf['عين']:
            ans.append(harf['سكون'])
        elif x[i] == harf[MEEM] and i - 1 >=0 and x[i-1] == harf[HAH] and i - 2 >=0 and x[i-2] == harf[FATHA] and i - 3 >=0 and x[i-3] == harf[REH] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[NOON]:
            ans.append(harf[MEEM])
            ans.append(harf[FATHA])
            ans.append(harf[ALEF])
            i = i + 1
        elif x[i] == harf[MEEM] and i - 1 >=0 and x[i-1] == harf[HAH] and i - 2 >=0 and x[i-2] == harf[FATHA] and i - 3 >=0 and x[i-3] == harf[SHADDA] and i - 4 >=0 and x[i-4] == harf[REH] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[NOON]:
            ans.append(harf[MEEM])
            # ans.append(harf[FATHA])
            ans.append(harf[ALEF])
            i = i + 1
        
        elif i - 1 >= 0 and x[i-1] == ' ' and x[i] == harf[LAM] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[KAF] and i + 3 < len(x) and x[i+3] == harf[KASRA] and i + 4 < len(x) and x[i+4] == harf[NOON]:
            if i + 5 < len(x) and x[i+5] == harf[SUKUN] and i + 6 < len(x) and x[i+6] == ' ':
                ans.append(harf[LAM])
                # ans.append(harf[FATHA])
                ans.append(harf[ALEF])
                i = i + 1
            elif i + 5 < len(x) and x[i+5] == harf[SHADDA] and i + 6 < len(x) and x[i+6] == harf[FATHA] :
                ans.append(harf[LAM])
                # ans.append(harf[FATHA])
                ans.append(harf[ALEF])
                i = i + 1 
        elif  x[i] == harf[HEH] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[THAL]   and i + 3 < len(x) and x[i+3] == harf[FATHA] and i + 4 < len(x) and x[i+4] == harf[ALEF] :
            ans.append(harf[HEH])
            ans.append(harf[ALEF])
            i = i + 1
        elif  x[i] == harf[HEH] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[THAL]   and i + 3 < len(x) and x[i+3] == harf[KASRA] and i + 4 < len(x) and x[i+4] == harf[HEH] and i + 5 < len(x) and x[i+5] == harf[KASRA] :
            ans.append(harf[HEH])
            ans.append(harf[ALEF])
            i = i + 1
        elif  x[i] == harf[THAL] and i + 1 < len(x) and x[i+1] == harf[KASRA] and i + 2 < len(x) and x[i+2] == harf[YEH] and i -1>=0 and x[i-1] == harf[LAM] and i - 2 >=0 and x[i-2] == harf[ALEF]  :
            ans.append(harf[LAM])
            ans.append(harf[FATHA])
            ans.append(harf[THAL])
            
        elif  x[i] == harf[TEH] and i + 1 < len(x) and x[i+1] == harf[KASRA] and i + 2 < len(x) and x[i+2] == harf[YEH] and i -1>=0 and x[i-1] == harf[LAM] and i - 2 >=0 and x[i-2] == harf[ALEF] :
            ans.append(harf[LAM])
            ans.append(harf[FATHA])
            ans.append(harf[TEH])
        elif  x[i] == harf[TAH] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[HEH] and i+3< len(x)  and x[i+3] == harf[FATHA] and (i+4< len(x) and (x[i+4] == ' ' or x[i+4] == '.' ) or i + 4 == len(x)) and i-1>=0 and x[i-1] == ' ':
            ans.append(harf[TAH])
            ans.append(harf[ALEF])
            i = i + 1
        elif  x[i] == harf[THAL] and i + 1 < len(x) and x[i+1] == harf[FATHA] and i + 2 < len(x) and x[i+2] == harf[LAM] and i+3< len(x) and x[i+3] == harf[KASRA] and i+4< len(x) and x[i+4] == harf[KAF] :
            ans.append(harf[THAL])
            ans.append(harf[ALEF])
            i=i+1
        else:
    #        print(x[i])
            ans.append(x[i])
        i = i + 1
    return ans

def del_sk(text):
    result = []
    for char in text:
        if char not in ['_ْ', harf[SUKUN],'\x01']:
            result.append(char)
    return result

def hamza_alef_teh_normalize(text):    
    text = araby.normalize_hamza(text)
    text = araby.normalize_alef(text)

    words_list = araby.spellit(text)
    text = words_list.split(',')
    text = del_sk(text)
    # print(text)
    for i in range(0, len(text)):
        if text[i] not in ["  ", " "]:
            text[i] = text[i].strip() 
        else:
            text[i] = ' '
        if text[i] not in [' ', '.', '،']:
            char_key = text[i]
            if char_key in harf:
                text[i] = harf[char_key]
            else:
                # إذا وجد رمزاً غريباً مثل \x01، يطبعه للتصحيح ويتجاهله
                print(f"Warning: Found unknown character {repr(char_key)}, skipping...")
                           
    
    for i in range(0, len(text)):
        if text[i] == harf['تاء مربوطة']:
            if i + 1 < len(text) and text[i+1] not in [harf['فتحة'], harf['ضمة'], harf['كسرة'], harf['فتحتان'], harf['كسرتان'], harf['ضمتان']]:
                text[i] = harf['ألف']
            elif i + 1 < len(text) and text[i+1] in [harf['فتحة'], harf['ضمة'], harf['كسرة'] ,harf['فتحتان'], harf['كسرتان'], harf['ضمتان']]:
                if (i + 2 < len(text) and text[i+2] == '.') or (i + 1 == len(text) - 1):
                    text[i] = harf['ألف']
                else :
                    text[i] = harf['تاء']
            elif (i == len(text) - 1):
                text[i] = harf['ألف']
        elif text[i] == harf['همزة']:
            if i + 1 < len(text) and text[i+1] == harf['همزة']:
                text[i+1] = harf['ألف']
    return text

def auto_tashkeel(text):
    text = "".join(ch for ch in str(text) if ch.isprintable())
    # Initialize the Vocalizer
    vocalizer = mishkal.tashkeel.TashkeelClass()    
    # Diacritize the text
    result = vocalizer.tashkeel(text)
    
    return result

def allah_word(text):
    if "لله" in text:
        text = text.replace("لله", "لّـلـٰه") 
    text = str(text).replace('ـ', '') # del tatweel
    return text

def main(inp):
    text = (str)(inp)
        
    # raw_text = ".ذهب الطالب إلى المدرسة"
    print(text)
    text = auto_tashkeel(text)
     
    text = "".join(ch for ch in str(text) if ch.isprintable())
    text = (str)(text).lstrip(' ')
    text = (str)(text).rstrip('\x01')
    print(text)
    # Output: ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ
    text = allah_word(text)
    print(text)
    ans = hamza_alef_teh_normalize(text)
    ans = al_alta3reef_and_alef_altafreeq_and_shadda_and_tanween(ans)
    print(ans)
    ind = set_indexes_noqta(ans)
    data = set_duration_and_pitch(ans, ind)
    convert_to_phofile(convert_to_phoneme(data))

if __name__ == "__main__":
    # الحصول على النص من معاملات سطر الأوامر
    # sys.argv[0] هو اسم الملف نفسه
    # sys.argv[1] هو المعامل الأول (النص الذي تم تمريره)
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("لا يوجد نص لتوليد الصوت منه.")
