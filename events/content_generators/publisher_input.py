def PublisherInput():
    return '''
        <form id="publisher_form" method="POST" action="publisher-save">
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
