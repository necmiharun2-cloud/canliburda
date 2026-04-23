import json
import requests

# Test Serper API integration
SERPER_API_KEY = input("Serper API Key'inizi girin (veya boş bırakın): ").strip()

if not SERPER_API_KEY:
    print("\nAPI Key girilmedi. Sadece bağlantı testi yapılacak.\n")
else:
    print("\nSerper API test ediliyor...\n")
    
    # Test search query
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "q": "bakır hurda fiyatı kg TL 2026",
        "gl": "tr",
        "hl": "tr"
    })
    
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✓ Serper API Bağlantısı BAŞARILI!")
            print(f"\nArama sonuçları bulundu: {len(data.get('organic', []))}")
            
            if 'organic' in data:
                print("\nİlk 3 sonuç:")
                for i, result in enumerate(data['organic'][:3], 1):
                    print(f"\n{i}. {result.get('title', 'Başlık yok')}")
                    print(f"   URL: {result.get('link', 'URL yok')}")
                    if 'snippet' in result:
                        snippet = result['snippet'][:150]
                        print(f"   {snippet}...")
        else:
            print(f"✗ Serper API Hatası: {response.status_code}")
            print(f"Yanıt: {response.text}")
            
    except Exception as e:
        print(f"✗ Bağlantı Hatası: {str(e)}")

print("\n" + "="*60)
print("Bot.py dosyasını çalıştırmak için:")
print("  python bot.py")
print("\nGUI açıldığında:")
print("  1. Serper API Key alanına key'inizi girin")
print("  2. 'API Key Kaydet' butonuna basın")
print("  3. 'BAŞLAT' butonuna basın")
print("="*60)
