import os
import openai
import logging

# Настройка API ключа
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_personalized_motivation(day, context):
    """Генерирует персонализированную мотивацию с помощью ChatGPT"""
    if not openai.api_key:
        return f"День {day}! Ты молодец! Продолжай в том же духе!"
    
    try:
        prompt = f"""
        Ты - мотивационный бот для людей, бросающих пить алкоголь. 
        Пользователь проходит {day}-й день 28-дневного трезвого челленджа. 
        За все дни у него было {context.get('total_urges', 0)} желаний выпить и 
        {context.get('total_thoughts', 0)} сохраненных мыслей.
        Напиши короткое мотивирующее сообщение (максимум 2 предложения) для этого пользователя.
        """
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помогаешь людям бросать пить алкоголь"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logging.error(f"AI motivation error: {e}")
        return f"День {day}! Ты молодец! Продолжай в том же духе!"

def generate_urge_support_message(day, urges_count):
    """Генерирует сообщение поддержки при желании выпить"""
    if not openai.api_key:
        return "Ты сильнее этого! Держись!"
    
    try:
        prompt = f"""
        Пользователь испытывает желание выпить алкоголь. Это уже {urges_count}-й раз за {day} дней трезвости.
        Напиши очень короткое (1 предложение) поддерживающее сообщение, чтобы помочь ему справиться с этим моментом.
        """
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помогаешь людям сопротивляться желанию выпить"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logging.error(f"AI urge support error: {e}")
        return "Ты сильнее этого! Держись!"

def generate_reflection_prompt(day):
    """Генерирует вопрос для саморефлексии"""
    if not openai.api_key:
        return "Как ты себя чувствуешь сегодня?"
    
    try:
        prompt = f"""
        Пользователь проходит {day}-й день трезвости. 
        Придумай один глубокий вопрос для саморефлексии, который поможет ему 
        осознать свои достижения и трудности на этом пути.
        """
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помогаешь людям осознанно проходить путь трезвости"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=80,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logging.error(f"AI reflection prompt error: {e}")
        return "Как ты себя чувствуешь сегодня?"