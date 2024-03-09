def ArticleInput():
    
    return '''
        <form id="article_form" method="POST" action="article-save">
            {{ form.hidden_tag() }}
            <div>
                {{ form.title.label }}
                {{ form.title(id="title") }}
                </div>
            <div>
                {{ form.content.label }}
                {{ form.content(id="content") }}
            </div>
            <div>
                {{ form.submit() }} 
            </div>
        </form>
    '''
