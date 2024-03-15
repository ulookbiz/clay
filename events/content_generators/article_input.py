def ArticleInput(nicks):
    
    ret = '''
        <form id="article_form" method="POST" action="article-save">
            {{ form.hidden_tag() }}
            <div>
                {{ form.title.label }}
                {{ form.title() }}
            </div>
            <div>
                {{ form.motto.label }}
                {{ form.motto() }}
            </div>
            <div>
                {{ form.ilink.label }}
                {{ form.ilink() }}
            </div>
            <div>
                {{ form.olink.label }}
                {{ form.olink() }}
            </div>
            <div>
                {{ form.content.label }}
                {{ form.content() }}
            </div>
            <div style="display: flex; justify-content: space-between;">
                <div>
                    {{ form.date_posted.label }}
                    {{ form.date_posted() }}
                </div>
                <div>
                    {{ form.date_pub.label }}
                    {{ form.date_pub() }}
                </div>    
                <div>    
                    {{ form.publisher_nick.label }}
                    {{ form.publisher_nick() }}
                </div>
                <div>
                    {{ form.submit() }} 
                </div>
            </div>
        </form>
    '''
    ret2="<div>"
    for nick in nicks:
        ret2 += "<span>"+nick+"</span> "
    ret2 += "</div>"

    return ret+ret2
