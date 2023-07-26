# Lib import
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from playsound import playsound

# Module import
from stt import request
from interface_module import interface
from stt import request

###################################################################################
###########   깃 커밋할 때 [main], [role]의 API KEY는 공란으로 입력해주세요    #############
##################################################################################

# OpenAI KEY
os.environ["OPENAI_API_KEY"] = ""
# PDF 로더 초기화
loader = PyPDFLoader("./story/kongji.pdf")
documents = loader.load()
# chunk : text를 자르는 단위, 1000글자당 1chunk
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 0)
documents = text_splitter.split_documents(documents)


def run():
    playsound("./mp3/start.mp3")
    menu_state = False 
    
    while True:
        # 사용자의 두번째 메뉴 선택부터 음성을 출력  
        if menu_state:
            playsound("./mp3/select_menu.mp3")

        command = request() 

        if not command:
            continue
        
        interface.handle_command(command, documents)
        menu_state = True

if __name__ == "__main__":
    run()