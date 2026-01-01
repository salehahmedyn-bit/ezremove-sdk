import asyncio
from ezremove import EzRemoveClient, EzRemoveError

async def main():
    # تمرير مفتاح تجريبي لتفادي خطأ الـ TypeError
    client = EzRemoveClient(api_key="YOUR_TEST_KEY")
    
    print("Testing EzRemove SDK...")
    try:
        # تجربة إرسال بيانات وهمية
        result = await client.remove_background(b"fake_image_data")
        print(f"Success! Result: {result}")
    except EzRemoveError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
