from dash import html

def Card(title, description, paragraph, width="w-full"):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H1(
                                title,
                                className="text-4xl font-bold tracking-tight text-zinc-100 sm:text-5xl",
                            ),
                            html.H2(
                                description,
                                className="mt-6 text-base text-zinc-400",
                            ),
                            html.Div(
                                [
                                    html.P(
                                        paragraph,
                                        className="text-zinc-400 mt-5 p-2",
                                    ),
                                ],
                                className="bg-white rounded-xl",
                            ),
                        ],
                        className="lg:order-first lg:row-span-2",
                    ),
                ],
                className="bg-black rounded-xl p-2",
            ),
        ],
        className=f"p-2 inline-block {width}",
    )

# grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 p-2

# grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3
        # children=[
        #     html.Div(
        #         children=[
        #             html.H2("Title", className="text-4xl font-bold tracking-tight text-zinc-100 sm:text-5xl"),
        #             html.P("Description", className="mt-6 text-base text-zinc-400"),
        #         ],
        #         className="lg:order-first lg:row-span-2"
        #     )
        # ],
        # className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 bg-green"


                    # html.Main(
                    #     children=[
                    #         html.Div(
                    #             children=children,
                    #             className="bg-orange-50 p-5 rounded-xl mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8"
                    #         )
                    #     ],
                    #     className="-mt-32 m-3.5"
                    # )

# <div class={cn('my-16 sm:mb-52 sm:mt-32')}>
# 	<div
# 		class="grid grid-cols-1 gap-y-16 lg:max-w-[700px] lg:grid-cols-1 lg:grid-rows-[auto_1fr] lg:gap-y-12"
# 	>
# 		<div class="lg:order-first lg:row-span-2">
# 			<h2 class="text-4xl font-bold tracking-tight text-zinc-100 sm:text-5xl">Contact</h2>
# 			<p class="mt-6 text-base text-zinc-400">
# 				Please feel free to contact me if you have any questions or would like to discuss a project.
# 			</p>
# 		</div>

# 		<Card.Root>
# 			<Card.Header>
# 				<Card.Title>Form</Card.Title>
# 				<Card.Description>
# 					Please fill out the form below and I'll get back to you as soon as possible.
# 				</Card.Description>
# 			</Card.Header>
# 			<Card.Content>
# 				<ContactForm data={data.form} />
# 			</Card.Content>
# 		</Card.Root>
# 	</div>
# </div>

# <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
# 					{#each categorized as { name, description, href, tags, host, state }}
# 						<a {href} class="group">
# 							<div class="flex h-full flex-col">
# 								<div class="flex h-full flex-col justify-between rounded-lg border p-4 shadow-md">
# 									<!-- Card content -->
# 									<h3 class="mb-2 text-xl font-semibold">{name}</h3>
# 									<p class="mb-4">{description}</p>
# 									<div class="flex flex-wrap gap-3">
# 										{#each tags as tag}
# 											<Badge>{tag}</Badge>
# 										{/each}
# 									</div>
# 									<div class="mt-8 flex items-center justify-between">
# 										<div class="flex items-center gap-2">
# 											<Link />
# 											<span class="group-hover:text-primary">{host}</span>
# 										</div>
# 										<span
# 											class={cn(`
#                                                 ${state === 'In Progress' ? 'group-hover:text-yellow-400' : ''}
#                                                 ${state === 'Completed' ? 'group-hover:text-green-400' : ''}
#                                             `)}>{state}</span
# 										>
# 									</div>
# 								</div>
# 							</div>
# 						</a>
# 					{/each}
# 				</div>