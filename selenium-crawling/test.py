try:
    from selenium import webdriver
    print("✅ selenium 정상 설치됨")
except ImportError as e:
    print("❌ selenium import 실패:", e)

print("hello world");