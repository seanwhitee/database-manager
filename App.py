import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from database import *
import pyperclip

def page_learning_background(conn):
    
    st.title("學歷")

    menu = ['Create', 'Read', "Update", 'Delete']
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == 'Update':

        st.markdown('### 你的學歷資料')
        background_df = read_learning_background_data(conn)
        st.dataframe(background_df)
        
        with st.form('更新學歷吧'):
            st.markdown('### 填入你要更新的學歷id')
            background_id = st.text_input('學歷id')
            
            st.markdown('### 填入修改後的資料')
            teacher_id = st.text_input('老師id')
            uni_name = st.text_input('大學')
            major = st.text_input('專業名')
            degree = st.text_input('學碩博')
            
            
            if st.form_submit_button('Update'):
                try:
                    update_background(conn, background_id, teacher_id, uni_name, major, degree)
                    st.success('成功更新 {}.'.format(f"{uni_name} {major} {degree}"))
                except Exception as e:
                    st.text(e)
        
    elif choice == 'Read':
        
        
        learning_background_df = read_learning_background_data(conn)
        st.dataframe(learning_background_df)
            
    elif choice == 'Create':
        with st.form('新增學歷吧'):
            st.markdown('### 填入你要新增的學歷資料')
            learning_background_id = st.text_input('學歷id')
            teacher_id = st.text_input('老師id')
            uni_name = st.text_input('大學', placeholder='ex: 逢甲大學')
            major = st.text_input('專業名', placeholder='ex: 資訊工程學系')
            degree = st.text_input('學碩博', placeholder='ex: 學士')
            
            if st.form_submit_button('Add'):
                try:
                    create_learning_background(conn, learning_background_id, teacher_id, uni_name, major, degree)
                    st.success('成功新增 {}.'.format(f"{uni_name} {major} {degree}"))
                except Exception as e:
                    st.text(e)

    elif choice == 'Delete':
        with st.form('刪除學歷'):
            st.markdown('### 填入你要刪除的學歷資料')
            deleted_background_id = st.text_input('學歷id')
            
            
            if st.form_submit_button('delete'):
                try:
                    delete_background(conn, deleted_background_id)
                    st.success('成功刪除 id {}.'.format(deleted_background_id))
                except Exception as e:
                    st.text(e)
                    
def page_journal(conn):       
    st.title("論文")

    menu = ['Create', 'Read', "Update", 'Delete']
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == 'Update':
        st.markdown('### 你的論文資料')
        journal_df = read_journal_data(conn)
        st.dataframe(journal_df)
        
        with st.form('更新論文吧'):
            st.markdown('### 填入你要更新的論文id')
            journal_id = st.text_input('論文id')
            
            st.markdown('### 填入修改後的資料')
            teacher_id = st.text_input('老師id')
            journal_name = st.text_input('論文名稱')
            journal_colaborator = st.text_area('共同合作者')
            journal_date = st.date_input('日期')
            journal_category = st.text_input('分類')
            
            if st.form_submit_button('Update'):
                try:
                    update_journal(conn, journal_id, teacher_id, journal_name,
                                journal_colaborator, journal_date, journal_category)
                    st.success('成功更新 {}.'.format(journal_name))
                except Exception as e:
                    st.text(e)
                    
    elif choice == 'Read':
        
        
        journal_df = read_journal_data(conn)
        st.dataframe(journal_df)
            
    elif choice == 'Create':
        
        with st.form('新增論文吧'):
            st.markdown('### 填入你要新增的論文資料')
            journal_id = st.text_input('論文id')
            teacher_id = st.text_input('老師id')
            journal_name = st.text_input('論文名稱')
            journal_colaborator = st.text_area('共同合作者')
            journal_date = st.date_input('日期')
            journal_category = st.text_input('分類')
            
            if st.form_submit_button('Add'):
                try:
                    create_journal(conn, journal_id, teacher_id, journal_name,
                                journal_colaborator, journal_date, journal_category)
                    st.success('成功新增 {}.'.format(journal_name))
                except Exception as e:
                    st.text(e)

    elif choice == 'Delete':
        with st.form('刪除論文'):
            st.markdown('### 填入你要刪除的論文資料')
            deleted_journal_id = st.text_input('論文id')
            deleted_journal_name = st.text_input('論文名稱')
            
            if st.form_submit_button('delete'):
                try:
                    delete_journal(conn, deleted_journal_id)
                    st.success('成功刪除 {}.'.format(deleted_journal_name))
                except Exception as e:
                    st.text(e)
                    
def page_exp(conn):

    st.title("經歷")

    menu = ['Create', 'Read', "Update", 'Delete']
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == 'Update':

        st.markdown('### 你的校內經歷資料')
        inner_exp_df = read_inner_exp_data(conn)
        st.dataframe(inner_exp_df)
        st.markdown('### 你的校外經歷資料')
        outer_exp_df = read_outer_exp_data(conn)
        st.dataframe(outer_exp_df)
        
        with st.form('更新經歷吧'):
            inner_or_outer = st.selectbox('經歷類型', ['校內', '校外'])
            st.markdown('### 填入你要更新的id')
            exp_id = st.text_input('經歷id')
            
            st.markdown('### 填入修改後的資料')
            teacher_id = st.text_input('老師id')
            location = st.text_input('任職地點')
            title = st.text_input('職稱')
            
            
            if st.form_submit_button('Update'):
                try:
                    if inner_or_outer == '校內':
                        update_inner_exp(conn, exp_id, teacher_id, location, title)
                    elif inner_or_outer == '校外':
                        update_outer_exp(conn, exp_id, teacher_id, location, title)
                    st.success('成功更新 {} id {}.'.format(inner_or_outer, exp_id))
                except Exception as e:
                    st.text(e)
        
    elif choice == 'Read':
        
        
        inner_exp_df = read_inner_exp_data(conn)
        outer_exp_df = read_outer_exp_data(conn)
        st.write('校內經歷')
        st.dataframe(inner_exp_df)
        st.write('校外經歷')
        st.dataframe(outer_exp_df)
            
    elif choice == 'Create':
        
        
        with st.form('新增經歷吧'):
            st.markdown('### 填入你要新增的經歷資料')
            inner_or_outer = st.selectbox('經歷類型', ['校內', '校外'])
            exp_id = st.text_input('經歷id')
            teacher_id = st.text_input('老師id')
            location = st.text_input('任職地點')
            title = st.text_input('職稱')
            
            
            if st.form_submit_button('Add'):
                try:
                    if inner_or_outer == '校內':
                        create_inner_exp(conn, exp_id, teacher_id, location, title)
                    elif inner_or_outer == '校外':
                        create_outer_exp(conn, exp_id, teacher_id, location, title)
                    
                    st.success('成功新增 {}.'.format(f"{inner_or_outer} {location} {title}"))
                    
                except Exception as e:
                    st.text(e)

    elif choice == 'Delete':
        with st.form('刪除經歷'):
            inner_or_outer = st.selectbox('經歷類型', ['校內', '校外'])
            st.markdown('### 填入你要刪除的經歷資料')
            
            deleted_id = st.text_input('經歷id')
            
            
            if st.form_submit_button('delete'):
                try:
                    if inner_or_outer == '校內':
                        delete_inner_exp(conn, deleted_id)
                    elif inner_or_outer == '校外':
                        delete_outer_exp(conn, deleted_id)
                    
                    st.success('成功刪除 {} id {}.'.format(inner_or_outer,  deleted_id)) 
                except Exception as e:
                    st.text(e)
                    
def page_talent(conn):
                  
    st.title("專長")

    menu = ['Create', 'Read', "Update", 'Delete']
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == 'Update':
        st.markdown('### 你的專長資料')
        talent_df = read_talent_data(conn)
        st.dataframe(talent_df)
        
        with st.form('更新專長吧'):
            st.markdown('### 填入你要更新的專長id')
            talent_id = st.text_input('專長id')
            
            st.markdown('### 填入修改後的資料')
            teacher_id = st.text_input('老師id')
            description = st.text_area('專長描述')
            
            
            if st.form_submit_button('Update'):
                try:
                    update_talent(conn, talent_id, teacher_id, description)
                    st.success('成功更新 {}.'.format(description))
                except Exception as e:
                    st.text(e)
    elif choice == 'Read':
        
        
        talent_df = read_talent_data(conn)
        st.dataframe(talent_df)
            
    elif choice == 'Create':
        with st.form('新增專長吧'):
            st.markdown('### 填入你要新增的專長資料')
            talent_id = st.text_input('專長id')
            teacher_id = st.text_input('老師id')
            talent_description = st.text_area('專長描述')
            
            
            if st.form_submit_button('Add'):
                try:
                    create_talent(conn, talent_id, teacher_id, talent_description)
                    st.success('成功新增 {}.'.format(talent_description))
                except Exception as e:
                    st.text(e)

    elif choice == 'Delete':
        with st.form('刪除專長'):
            st.markdown('### 填入你要刪除的專長資料')
            deleted_talent_id = st.text_input('專長id')
            
            
            if st.form_submit_button('delete'):
                try:
                    delete_talent(conn, deleted_talent_id)
                    st.success('成功刪除 id {}.'.format(deleted_talent_id))
                except Exception as e:
                    st.text(e)
                    
def page_courses(conn):
    st.title("課表")

    menu = ['Create', 'Read', "Update", 'Delete']
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == 'Update':
        st.markdown('### 你的課表資料')
        courses_df = read_course_table_data(conn)
        st.dataframe(courses_df)
        
        with st.form('更新課表吧'):
            st.markdown('### 填入你要更新的課程id')
            course_id = st.text_input('課程id')
            
            st.markdown('### 填入修改後的資料')
            teacher_id = st.text_input('老師id')
            course_name = st.text_input('課程名稱')
            
            # let user select class time
            class_time_map = {
                '第一節': 1,
                '第二節': 2,
                '第三節': 3,
                '第四節': 4,
                '第五節': 5,
                '第六節': 6,
                '第七節': 7,
                '第八節': 8,
                '第九節': 9,
                '第十節': 10,
                '第十一節': 11,
                '第十二節': 12,
                '第十三節': 13,
                '第十四節': 14
            }
            class_time = st.selectbox('第幾節', options=class_time_map.keys())
            
            day_in_weeks = ['一', '二', '三', '四', '五', '六', '日']
            day_in_week = st.selectbox('星期幾', options= day_in_weeks)
            
            
            if st.form_submit_button('Update'):
                try:
                    update_course(conn, course_id, teacher_id, course_name, class_time_map[class_time], day_in_week)
                    st.success('成功更新 {}.'.format(course_name))
                except Exception as e:
                    st.text(e)
        
    elif choice == 'Read':
        
        
        courses_df = read_course_table_data(conn)
        st.dataframe(courses_df)
            
    elif choice == 'Create':
        
        with st.form('新增課表吧'):
            st.markdown('### 填入你要新增的課程資料')
            course_id = st.text_input('課程id')
            teacher_id = st.text_input('老師id')
            course_name = st.text_input('課程名稱')
            # let user select class time
            class_time_map = {
                '第一節': 1,
                '第二節': 2,
                '第三節': 3,
                '第四節': 4,
                '第五節': 5,
                '第六節': 6,
                '第七節': 7,
                '第八節': 8,
                '第九節': 9,
                '第十節': 10,
                '第十一節': 11,
                '第十二節': 12,
                '第十三節': 13,
                '第十四節': 14
            }
            class_time = st.selectbox('第幾節',options= class_time_map.keys())
            
            day_in_weeks = ['一', '二', '三', '四', '五', '六', '日']
            day_in_week = st.selectbox('星期幾', options= day_in_weeks)
            
            if st.form_submit_button('Add'):
                try:
                    create_courses(conn, course_id, teacher_id, course_name, class_time_map[class_time], day_in_week)
                    st.success('成功新增 {}.'.format(course_name))
                except Exception as e:
                    st.text(e)
            
                
    elif choice == 'Delete':
        with st.form('刪除課程'):
            st.markdown('### 填入你要刪除的課程資料')
            deleted_course_id = st.text_input('課程id')
            deleted_course_name = st.text_input('課程名稱')
            
            if st.form_submit_button('delete'):
                try:
                    delete_course(conn, deleted_course_id)
                    st.success('成功刪除 {}.'.format(deleted_course_name))
                except Exception as e:
                    st.text(e)
                
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
  
def main():
    
    connect_db = connect()  
    create_table_if_not_exist(connect_db)
    
    # set each cloumn width to max
    pd.set_option('display.max_colwidth', None)
    
    # use css       
    local_css("style.css")
        
    with st.sidebar:
        bar = option_menu(
            menu_title= 'IECS',
            menu_icon='house',
            options=['論文','專長','學歷','經歷','課表'],
            
        )

        if bar == "論文":
            page_journal(connect_db)
                    
        elif bar == "專長":
            page_talent(connect_db)
            
        elif bar == "學歷":            
            page_learning_background(connect_db)

        elif bar == "經歷":
            page_exp(connect_db)
            
        elif bar == "課表":
            page_courses(connect_db)
    
    # Begining of the main page content
    
    col1, col2  = st.columns(2)
    with col1:
        st.markdown('# ... 教授')
        st.markdown('### ...description...')
        
        if st.button('信箱 : email...', use_container_width=True):
            text_to_be_copied = 'email...'
            pyperclip.copy(text_to_be_copied)

        if st.button('分機 : phone number...', use_container_width=True):
            text_to_be_copied = 'phone number...'
            pyperclip.copy(text_to_be_copied)
            
        with st.expander('課表時間'):
            courses_table_df = read_course_table_data(connect_db)
            st.dataframe(courses_table_df, use_container_width=True)
    
    with col2:
        st.image('./assets/imgs/dbs-test-image.jpg', use_column_width=True)
        
        
    # learning background / talent column
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="content-category-child-bar"><strong><span class="content-category-text">學歷</span><strong></div>', unsafe_allow_html=True)
        leaning_background_df = read_learning_background_data(connect_db)
        
        st.dataframe(leaning_background_df, use_container_width=True)
    with col4:
        st.markdown('<div class="content-category-child-bar"><strong><span class="content-category-text">專長</span></strong></div>', unsafe_allow_html=True)
        talent_df = read_talent_data(connect_db)
        st.dataframe(talent_df, use_container_width=True)
        
    # inner-experience / outer-experience column
    col5, col6 = st.columns(2)
    with col5:
        st.markdown('<div class="content-category-child-bar"><strong><span class="content-category-text">校內經歷</span></strong></div>', unsafe_allow_html=True)
        inner_exp_df = read_inner_exp_data(connect_db)
        st.dataframe(inner_exp_df, use_container_width=True)
    with col6:
        st.markdown('<div class="content-category-child-bar"><strong><span class="content-category-text">校外經歷</span></strong></div>', unsafe_allow_html=True)
        outer_exp_df = read_outer_exp_data(connect_db)
        st.dataframe(outer_exp_df, use_container_width=True)
    
    # journal column
    st.markdown('<div class="content-category-child-bar"><strong><span class="content-category-text">論文</span><strong></div>', unsafe_allow_html=True)
    journal_df = read_journal_data(connect_db)
    st.dataframe(journal_df, use_container_width=True)

    # line break before footer
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
        
    # Add line before page footer
    st.markdown("""<hr class="between-footer-and-content">""", unsafe_allow_html=True)
 
    # Contact us
    st.write('聯絡我們')
    fast_link_col1, fast_link_col2 = st.columns(2)
    
    with fast_link_col1:
        # some hyperlink
        st.markdown("""<a href="https://www.fcu.edu.tw/" class="">逢甲大學</p>""", unsafe_allow_html=True)
        st.markdown("""<a href="https://www.checkinatfcu.com/" class="">逢城學記</p>""", unsafe_allow_html=True)
        st.markdown("""<a href="https://ilearn2.fcu.edu.tw/" class="">ilearn2.0</p>""", unsafe_allow_html=True)
        st.markdown("""<a href="https://coiee.fcu.edu.tw/" class="">資訊電機學院</p>""", unsafe_allow_html=True)
        
    with fast_link_col2:
        
        # streamlit expander for streamlit map chart
        with st.expander("逢甲大學資訊電機館2樓"):
            
            # Prepare map data for fcu map chart
            df = {'latitude': [24.1793208789036], 'longitude': [120.65010804950602]}
            fcu_map_data = pd.DataFrame(df)
            
            # fcu map chart
            st.map(fcu_map_data, zoom=13)
        
        st.markdown("""聯絡電話 : <a href="tel:123-456-7890" target="_self" class="">0424517250#3701</a>""", unsafe_allow_html=True)
        st.markdown("""聯絡信箱 : <a href="mailto:iecs@fcu.edu.tw" class=""> iecs@fcu.edu.tw </a>""", unsafe_allow_html=True)
        
if __name__ == '__main__':
    main()
    
    
