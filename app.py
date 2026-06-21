import streamlit as st
st.markdown("""
    <style>
            [data-testid="stAppViewContainer"] {
                        direction: rtl;s
                                    text-align: right;
                                            }
                                                </style>
                                                """, unsafe_allow_html=True)
# 1. إعدادات الصفحة والعنوان الرهيب بحركة الفراشات
st.set_page_config(page_title="منصة الفراشة", page_icon="🦋")
st.title("🦋 منصة الفراشة لتعليم الأزمنة 🦋")
st.write(".دليلكِ السريع لإتقان قواعد اللغة الإنجليزية والأزمنة بشكل مبسط")

st.markdown("---")
st.subheader(":اكتشفي الأزمنة والقواعد")

# 2. قائمة الأزمنة الشاملة (9 أزمنة)
azmena_list = [
    "المضارع البسيط (Present Simple)",
    "الماضي البسيط (Past Simple)",
    "المستقبل البسيط (Future Simple)",
    "المضارع المستمر (Present Continuous)",
    "الماضي المستمر (Past Continuous)",
    "المستقبل المستمر (Future Continuous)",
    "المضارع التام (Present Perfect)",
    "الماضي التام (Past Perfect)",
    "المستقبل التام (Future Perfect)"
]

zaman = st.selectbox(":اختر الزمن الذي تريد مراجعته", azmena_list)

st.markdown("---")

# 3. الشروط وعرض الشرح لكل زمن بالتفصيل والمسافات المضبوطة
if zaman == "المضارع البسيط (Present Simple)":
    st.info("### 💡 المضارع البسيط (Present Simple)")
    st.write(".الاستخدام: للأحداث المتكررة، العادات، والحقائق الثابتة")
    st.write(":التركيب")
    st.code("He/She/It + Verb(s)\nI/We/They/You + Verb (inf)")
    st.write(":أمثلة")
    st.success("• She studies English every day.")

elif zaman == "الماضي البسيط (Past Simple)":
    st.info("### ⏳ الماضي البسيط (Past Simple)")
    st.write(".الاستخدام: لأحداث بدأت وانتهت في الماضي في وقت محدد")
    st.write(":التركيب")
    st.code("Subject + Verb-ed (or irregular verb)")
    st.write(":أمثلة")
    st.success("• I visited my friend yesterday.")

elif zaman == "المستقبل البسيط (Future Simple)":
    st.info("### 🔮 المستقبل البسيط (Future Simple)")
    st.write(".الاستخدام: للتنبؤات، القرارات السريعة، أو الخطط المستقبلية")
    st.write(":التركيب")
    st.code("Subject + will + Verb (inf)")
    st.write(":أمثلة")
    st.success("• We will travel next week.")

elif zaman == "المضارع المستمر (Present Continuous)":
    st.info("### 🔄 المضارع المستمر (Present Continuous)")
    st.write(".الاستخدام: لحدث يحدث الآن في لحظة الكلام")
    st.write(":التركيب")
    st.code("Am/Is/Are + Verb + -ing")
    st.write(":أمثلة")
    st.success("• She is studying English right now.")

elif zaman == "الماضي المستمر (Past Continuous)":
    st.info("### 🎬 الماضي المستمر (Past Continuous)")
    st.write(".الاستخدام: لحدث كان مستمراً في وقت معين في الماضي عندما قطعه حدث آخر")
    st.write(":التركيب")
    st.code("Was/Were + Verb + -ing")
    st.write(":أمثلة")
    st.success("• I was watching TV when you called.")

elif zaman == "المستقبل المستمر (Future Continuous)":
    st.info("### 🚀 المستقبل المستمر (Future Continuous)")
    st.write(".الاستخدام: لحدث سيكون مستمراً في وقت محدد في المستقبل")
    st.write(":التركيب")
    st.code("Subject + will be + Verb + -ing")
    st.write(":أمثلة")
    st.success("• At this time tomorrow, I will be flying to Dubai.")

elif zaman == "المضارع التام (Present Perfect)":
    st.info("### ✅ المضارع التام (Present Perfect)")
    st.write(".الاستخدام: لحدث تم في الماضي وله أثر في الحاضر، أو تجارب الحياة بدون تحديد وقت")
    st.write(":التركيب")
    st.code("Has/Have + Verb (v3 - Past Participle)")
    st.write(":أمثلة")
    st.success("• I have lived here for 5 years.")

elif zaman == "الماضي التام (Past Perfect)":
    st.info("### 📜 الماضي التام (Past Perfect)")
    st.write(".الاستخدام: لحدث وقع وانتهى قبل حدث آخر في الماضي (الحدث الأول)")
    st.write(":التركيب")
    st.code("Subject + had + Verb (v3 - Past Participle)")
    st.write(":أمثلة")
    st.success("• The train had left before I arrived at the station.")

elif zaman == "المستقبل التام (Future Perfect)":
    st.info("### 🏁 المستقبل التام (Future Perfect)")
    st.write(".الاستخدام: لحدث سيكون قد اكتمل وانتهى قبل وقت معين في المستقبل")
    st.write(":التركيب")
    st.code("Subject + will have + Verb (v3 - Past Participle)")
    st.write(":أمثلة")
    st.success("• By 2027, I will have graduated from university.")

st.markdown("---")
st.caption("صنع بكل حب في منصة الفراشة 🦋")