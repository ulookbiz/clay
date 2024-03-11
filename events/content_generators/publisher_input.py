def PublisherInput():
    return '''
        <form id="publisher_form" method="POST" action="publisher-save">
            {{ form.hidden_tag() }}
            <div>
                {{ form.pub_name.label }}
                {{ form.pub_name() }}
                </div>
            <div>
                {{ form.nick.label }}
                {{ form.nick() }}
            </div>
            <div>
                {{ form.pub_status.label }}
                {{ form.pub_status() }}
            </div>
            <div>
                {{ form.reference.label }}
                {{ form.reference() }}
            </div>
            <div>
                {{ form.emblem.label }}
                {{ form.emblem() }}
            </div>
            <div>
                {{ form.submit() }} 
            </div>
        </form>
    '''
