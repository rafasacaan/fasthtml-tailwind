from fasthtml.components import *

content = Body(
    Div(
        Div(
            H1('Landing', cls='font-serif text-3xl font-medium'),
            A('Get this template', href='https://github.com/gary149/landing-gradients', cls='self-start px-3 py-2 leading-none text-gray-200 border border-gray-800 rounded-lg focus:outline-none focus:shadow-outline bg-gradient-to-b hover:from-indigo-500 from-gray-900 to-black'),
            cls='flex justify-between'
        ),
        Div(cls='h-32 md:h-40'),
        P('Spend less time coding and more time creating', cls='font-sans text-4xl font-bold text-gray-200 max-w-5xl lg:text-7xl lg:pr-24 md:text-6xl'),
        Div(cls='h-10'),
        P('Imagine being able to spent less time... This is a demonstration landing\n            page made with tailwindcss', cls='max-w-2xl font-serif text-xl text-gray-400 md:text-2xl'),
        Div(cls='h-32 md:h-40'),
        Div(
            Div(
                P('Simple and easy', cls='self-start inline font-sans text-xl font-medium text-transparent bg-clip-text bg-gradient-to-br from-green-400 to-green-600'),
                H2('Made for devs and designers', cls='text-4xl font-bold'),
                Div(cls='h-6'),
                P('Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam\n                    autem, a recusandae vero praesentium qui impedit doloremque\n                    molestias necessitatibus.', cls='font-serif text-xl text-gray-400 md:pr-10'),
                Div(cls='h-8'),
                Div(
                    Div(
                        P('Made with love', cls='font-semibold text-gray-400'),
                        Div(cls='h-4'),
                        P('Lorem ipsum dolor sit, amet consectetur adipisicing elit.\n                            Delectus labor.', cls='font-serif text-gray-400')
                    ),
                    Div(
                        P("It's easy to build", cls='font-semibold text-gray-400'),
                        Div(cls='h-4'),
                        P('Ipsum dolor sit, amet consectetur adipisicing elit. Delectus\n                            amet consectetur.', cls='font-serif text-gray-400')
                    ),
                    cls='grid grid-cols-2 gap-4 pt-8 border-t border-gray-800'
                ),
                cls='flex flex-col justify-center'
            ),
            Div(
                Div(cls='-mr-24 rounded-lg md:rounded-l-full bg-gradient-to-br from-gray-900 to-black h-96')
            ),
            cls='grid gap-8 md:grid-cols-2'
        ),
        Div(cls='h-32 md:h-40'),
        P(
            Span('If we work all together', cls='text-gray-400'),
            Span('consectetur adipisicing elit. Consectetur atque molestiae omnis\n          excepturi enim!', cls='text-gray-600'),
            cls='font-serif text-4xl'
        ),
        Div(cls='h-32 md:h-40'),
        Div(
            Div(
                P('1', cls='flex items-center justify-center text-4xl font-semibold text-green-400 bg-green-800 rounded-full shadow-lg w-14 h-14'),
                Div(cls='h-6'),
                P('We build products with UX in mind', cls='font-serif text-3xl'),
                cls='flex-col p-8 py-16 rounded-lg shadow-2xl md:p-12 bg-gradient-to-br from-gray-900 to-black'
            ),
            Div(
                P('2', cls='flex items-center justify-center text-4xl font-semibold text-indigo-400 bg-indigo-800 rounded-full shadow-lg w-14 h-14'),
                Div(cls='h-6'),
                P('You can trust us to deliver super fast', cls='font-serif text-3xl'),
                cls='flex-col p-8 py-16 rounded-lg shadow-2xl md:p-12 bg-gradient-to-b from-gray-900 to-black'
            ),
            Div(
                P('3', cls='flex items-center justify-center text-4xl font-semibold text-teal-400 bg-teal-800 rounded-full shadow-lg w-14 h-14'),
                Div(cls='h-6'),
                P('We made it simple and easy to do', cls='font-serif text-3xl'),
                cls='flex-col p-8 py-16 rounded-lg shadow-2xl md:p-12 bg-gradient-to-bl from-gray-900 to-black'
            ),
            cls='grid gap-4 md:grid-cols-3'
        ),
        Div(cls='h-40'),
        Div(
            Div(
                P('We are humans', cls='self-start inline font-sans text-xl font-medium text-transparent bg-clip-text bg-gradient-to-br from-teal-400 to-teal-600'),
                H2('We could work together', cls='text-4xl font-bold'),
                Div(cls='h-6'),
                P('Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magnam\n                    autem, a recusandae vero praesentium qui impedit doloremque\n                    molestias.', cls='font-serif text-xl text-gray-400 md:pr-10'),
                Div(cls='h-8'),
                Div(
                    Div(
                        P('Made with love', cls='font-semibold text-gray-400'),
                        Div(cls='h-4'),
                        P('Lorem ipsum dolor sit, amet consectetur adipisicing elit.\n                            Delectus labor.', cls='font-serif text-gray-400')
                    ),
                    Div(
                        P("It's easy to build", cls='font-semibold text-gray-400'),
                        Div(cls='h-4'),
                        P('Ipsum dolor sit, amet consectetur adipisicing elit. Delectus\n                            amet consectetur.', cls='font-serif text-gray-400')
                    ),
                    Div(
                        P("It's easy to build", cls='font-semibold text-gray-400'),
                        Div(cls='h-4'),
                        P('Ipsum dolor sit, amet consectetur adipisicing elit. Delectus\n                            amet consectetur.', cls='font-serif text-gray-400')
                    ),
                    cls='grid gap-6 pt-8 border-t border-gray-800 lg:grid-cols-3'
                ),
                cls='flex flex-col justify-center md:col-span-2'
            ),
            Div(
                Div(cls='-mr-24 rounded-lg md:rounded-l-full bg-gradient-to-br from-gray-900 to-black h-96')
            ),
            cls='grid gap-8 md:grid-cols-3'
        ),
        Div(cls='h-10 md:h-40'),
        Div(
            Ul(
                Li('Social networks', cls='pb-4 font-serif text-gray-400'),
                Li(
                    A('Twitter', href='https://twitter.com/victormustar', cls='hover:underline')
                ),
                Li(
                    A('Linkedin', href='#', cls='hover:underline')
                ),
                Li(
                    A('Facebook', href='#', cls='hover:underline')
                ),
                cls='space-y-1 text-gray-400'
            ),
            Ul(
                Li('Locations', cls='pb-4 font-serif text-gray-400'),
                Li(
                    A('Paris', href='#', cls='hover:underline')
                ),
                Li(
                    A('New York', href='#', cls='hover:underline')
                ),
                Li(
                    A('London', href='#', cls='hover:underline')
                ),
                Li(
                    A('Singapour', href='#', cls='hover:underline')
                ),
                cls='space-y-1 text-gray-400'
            ),
            Ul(
                Li('Company', cls='pb-4 font-serif text-gray-400'),
                Li(
                    A('The team', href='#', cls='hover:underline')
                ),
                Li(
                    A('About us', href='#', cls='hover:underline')
                ),
                Li(
                    A('Our vision', href='#', cls='hover:underline')
                ),
                Li(
                    A('Join us', href='#', cls='hover:underline')
                ),
                cls='space-y-1 text-gray-400'
            ),
            Ul(
                Li('Join', cls='pb-4 font-serif text-gray-400'),
                Li(
                    A('Get this template', href='https://github.com/gary149/landing-gradients', cls='self-start px-3 py-2 leading-none text-gray-200 border border-gray-800 rounded-lg focus:outline-none focus:shadow-outline bg-gradient-to-b hover:from-indigo-500 from-gray-900 to-black')
                ),
                cls='space-y-1 text-gray-400'
            ),
            cls='grid gap-4 md:grid-cols-4'
        ),
        Div(cls='h-12'),
        cls='text-gray-300 container mx-auto p-8 overflow-hidden md:rounded-lg md:p-10 lg:p-12'
    ),
    cls='bg-gradient-to-br from-gray-900 to-black'
)