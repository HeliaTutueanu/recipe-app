from recipes.models import Recipe
from io import BytesIO  
import base64
import matplotlib.pyplot as plt

def get_recipename_from_id(val):
    recipename=Recipe.objects.get(id=val)
    #and the name is returned back 
    return recipename


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(6,5), facecolor="none")

    if chart_type == 'bar_chart':
        plt.rcParams.update({'axes.facecolor': 'none'})
        plt.bar(data['name'], data['cooking_time'], color='#525a81')
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time in min')
        plt.xticks(rotation=35, ha='right')
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.title('Recipes by Cooking Time')

    elif chart_type == 'pie_chart':
        difficulty_counts = data['difficulty'].value_counts()
        labels = difficulty_counts.index
        values = difficulty_counts.values
        plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['#4f5e7c', '#acbde2', '#525a81', '#53BD99'])
        plt.title('Recipes by Difficulty')

    elif chart_type == 'line_chart':
        plt.rcParams.update({'axes.facecolor': 'none'})
        data['formatted_date'] = data['date_created'].apply(lambda x: x.strftime('%Y-%m-%d'))
        recipes_per_day = data.groupby(data['formatted_date']).size()
        plt.plot(recipes_per_day.index, recipes_per_day, color='#525a81')
        plt.xlabel('Date Created')
        plt.ylabel('Number of Recipes')
        plt.title('Number of Recipes Created per Day')
        plt.xticks(rotation=35, ha='right')
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        
    else:
        print ('Unknown chart type')
    
    plt.tight_layout()

    chart =get_graph()  
    return chart        