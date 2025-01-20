from fasthtml.components import *

content = Div(
    H2('Services', cls='mb-1 text-3xl font-extrabold leading-tight text-gray-900'),
    P('Here is a few of the awesome Services we provide.', cls='mb-12 text-lg text-gray-500'),
    Div(
        Div(
            Div(
                Div(
                    Span(cls='absolute top-0 left-0 w-full h-full mt-1 ml-1 bg-indigo-500 rounded-lg'),
                    Div(
                        Div(
                            H3('DAPP Development', cls='my-2 ml-3 text-lg font-bold text-gray-800'),
                            cls='flex items-center -mt-1'
                        ),
                        P('------------', cls='mt-3 mb-1 text-xs font-medium text-indigo-500 uppercase'),
                        P('A decentralized application (dapp) is an application built on a\n                            decentralized network that combines a smart contract and a frontend user interface.', cls='mb-2 text-gray-600'),
                        cls='relative h-full p-5 bg-white border-2 border-indigo-500 rounded-lg'
                    ),
                    cls='relative h-full ml-0 mr-0 sm:mr-10'
                ),
                cls='w-full mb-10 sm:mb-0 sm:w-1/2'
            ),
            Div(
                Div(
                    Span(cls='absolute top-0 left-0 w-full h-full mt-1 ml-1 bg-purple-500 rounded-lg'),
                    Div(
                        Div(
                            H3('Web 3.0 Development', cls='my-2 ml-3 text-lg font-bold text-gray-800'),
                            cls='flex items-center -mt-1'
                        ),
                        P('------------', cls='mt-3 mb-1 text-xs font-medium text-purple-500 uppercase'),
                        P('Web 3.0 is the third generation of Internet services that will\n                            focus on understanding and analyzing data to provide a semantic web.', cls='mb-2 text-gray-600'),
                        cls='relative h-full p-5 bg-white border-2 border-purple-500 rounded-lg'
                    ),
                    cls='relative h-full ml-0 md:mr-10'
                ),
                cls='w-full sm:w-1/2'
            ),
            cls='flex flex-col w-full mb-10 sm:flex-row'
        ),
        Div(
            Div(
                Div(
                    Span(cls='absolute top-0 left-0 w-full h-full mt-1 ml-1 bg-blue-400 rounded-lg'),
                    Div(
                        Div(
                            H3('Project Audit', cls='my-2 ml-3 text-lg font-bold text-gray-800'),
                            cls='flex items-center -mt-1'
                        ),
                        P('------------', cls='mt-3 mb-1 text-xs font-medium text-blue-400 uppercase'),
                        P('A Project Audit is a formal review of a project, which is intended\n                            to assess the extent up to which project management standards are being upheld.', cls='mb-2 text-gray-600'),
                        cls='relative h-full p-5 bg-white border-2 border-blue-400 rounded-lg'
                    ),
                    cls='relative h-full ml-0 mr-0 sm:mr-10'
                ),
                cls='w-full mb-10 sm:mb-0 sm:w-1/2'
            ),
            Div(
                Div(
                    Span(cls='absolute top-0 left-0 w-full h-full mt-1 ml-1 bg-yellow-400 rounded-lg'),
                    Div(
                        Div(
                            H3('Hacking / RE', cls='my-2 ml-3 text-lg font-bold text-gray-800'),
                            cls='flex items-center -mt-1'
                        ),
                        P('------------', cls='mt-3 mb-1 text-xs font-medium text-yellow-400 uppercase'),
                        P('A security hacker is someone who explores methods for breaching\n                            defenses and exploiting weaknesses in a computer system or network.', cls='mb-2 text-gray-600'),
                        cls='relative h-full p-5 bg-white border-2 border-yellow-400 rounded-lg'
                    ),
                    cls='relative h-full ml-0 mr-0 sm:mr-10'
                ),
                cls='w-full mb-10 sm:mb-0 sm:w-1/2'
            ),
            Div(
                Div(
                    Span(cls='absolute top-0 left-0 w-full h-full mt-1 ml-1 bg-green-500 rounded-lg'),
                    Div(
                        Div(
                            H3('Bot/Script Development', cls='my-2 ml-3 text-lg font-bold text-gray-800'),
                            cls='flex items-center -mt-1'
                        ),
                        P('------------', cls='mt-3 mb-1 text-xs font-medium text-green-500 uppercase'),
                        P('Bot development frameworks were created as advanced software tools\n                            that eliminate a large amount of manual work and accelerate the development process.', cls='mb-2 text-gray-600'),
                        cls='relative h-full p-5 bg-white border-2 border-green-500 rounded-lg'
                    ),
                    cls='relative h-full ml-0 md:mr-10'
                ),
                cls='w-full sm:w-1/2'
            ),
            cls='flex flex-col w-full mb-5 sm:flex-row'
        ),
        cls='w-full'
    ),
    cls='container relative flex flex-col justify-between h-full max-w-6xl px-10 mx-auto xl:px-0 mt-5'
)
