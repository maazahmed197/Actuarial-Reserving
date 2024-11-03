import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
# from streamlit_agraph import agraph, Node, Edge, Config
# import graphviz
import numpy as np




# Chapter 1: Introduction
def chapter_1():
    st.header("Chapter 1: Introduction to Reserves and Claims")
    st.subheader("Reserving")
    st.write("""
    The term **reserves** in insurance can be complex, as it covers multiple types of reserves 
    seen in financial statements, including:
    
    - **Case Reserves**: Amount set aside for known claims with estimates based on current information.
    - **Loss Reserves**: Funds held to pay future claims on already occurred events.
    - **Bulk and IBNR Reserves**: Includes reserves for claims that are incurred but not reported.
    - **Case LAE Reserves**: Reserves for Loss Adjustment Expenses, related to managing the claim.
    - Other reserves such as unearned premium reserves, reserves for bad debts, rate credits, 
      general and contingency reserves, and earthquake reserves.

    For this guide, we focus on estimating unpaid claims and claim adjustment expenses, often called 
    **unpaid claim estimates** as defined by ASOP 43. Unlike general "reserves," unpaid claim estimates 
    refer to an actuary's specific estimate of future obligations from past claims. 

    #### Key Components of Unpaid Claim Estimates

    The unpaid claims estimate consists of five primary components:
    1. **Case Outstanding on Known Claims**: Estimates by claims departments for known and reported claims only.
    2. **Provision for Future Development on Known Claims**: Adjustments for further development.
    3. **Estimate for Reopened Claims**: Reserves for claims that may reopen in the future.
    4. **Provision for Claims Incurred But Not Reported (IBNR)**: Claims that have occurred but are not yet reported.
    5. **Provision for Claims in Transit**: Claims that are reported but not yet recorded.

    #### IBNR Breakdown

    Actuaries typically use **IBNR** in a broad sense to cover:
    - **Incurred But Not Yet Reported Claims (Pure IBNR)**: Claims incurred but not yet reported.
    - **Incurred But Not Enough Reported (IBNER)**: Development on known claims that may need further adjustment.
    
    Differentiating between these components helps in evaluating the adequacy of case outstanding and 
    supports management decisions on unpaid claim estimates.

    #### Claims, Losses, and Claim Counts
             
    In this text, we use the term claims instead of losses, as it aligns with the terminology commonly used in U.S. and Canadian actuarial standards and financial reporting.
    While the terms are often interchangeable, our choice aims for consistency and clarity, particularly when referring to ultimate claims, expected claims, claim ratios, and claim adjustment expenses.
    We also distinguish between claims (monetary values) and claim counts (the number of claims).
             
    #### Reported Claims
             
    We adopt the term reported claims rather than incurred claims to avoid confusion regarding the inclusion of incurred but not reported (IBNR) claims.
    Reported claims generally encompass the sum of cumulative paid claims and case outstanding estimates at a specific time. 
    In certain contexts, we may refer to incremental reported claims instead of cumulative ones.
             
    #### Ultimate Claims
             
    Ultimate claims represent the total dollar value once all claims are settled and closed, with no possibility of reopening. 
    For short-tail insurance lines, such as property insurance, ultimate claims can typically be estimated within one or two years post-accident. 
    However, for long-tail lines, like general liability and workers' compensation, it may take many years or even decades to ascertain ultimate claims. 
    A critical aspect of estimating unpaid claims is projecting ultimate claims, which serves as the foundation for calculating unpaid claims for IBNR and total unpaid estimates.
    
    #### Claim-Related Expenses
             
    We refer to claim adjustment expenses and claim-related expenses collectively to encompass total claim adjustment expenses, which include both allocated loss adjustment expenses (ALAE) and unallocated loss adjustment expenses (ULAE). 
    The terminology of ALAE and ULAE is retained due to its widespread acceptance. 
    Throughout our examples, claims include ALAE but exclude ULAE unless otherwise noted.
    """)

    st.markdown("### Concept Summary")
    st.write("""
    This chapter provides foundational knowledge on reserves and unpaid claims estimates, 
    with terminology aligned to ASOP 43 standards. Understanding these definitions is crucial for 
    accurate reserving practices and communication within the field of actuarial science.
    """)
    st.markdown("---")

# Chapter 2: Claims Process
def chapter_2():
    st.header("Chapter 2: The Claims Process and Estimation of Unpaid Claims")
    st.write("""
    The estimation of unpaid claims involves several components:

    1. **Case Outstanding**: Known claims with an estimate based on current information.
    2. **Provision for Future Development on Known Claims**: Adjustments for further development.
    3. **Estimate for Reopened Claims**: Reserves for claims that may reopen.
    4. **Provision for IBNR (Incurred But Not Reported)**: Claims that have occurred but are not reported.
    5. **Provision for Claims in Transit**: Claims that are in the process of reporting.

    The chart below visualizes these five estimates.
    """)

    # st.title("Claims Estimation Process")
    # st.subheader("Components of Unpaid Claims")

    # # Define the components and their descriptions
    # components = [
    #     "Case Outstanding",
    #     "Provision for Future Development",
    #     "Estimate for Reopened Claims",
    #     "Provision for IBNR",
    #     "Provision for Claims in Transit"
    # ]
    # descriptions = [
    #     "Estimates for known claims based on current information.",
    #     "Additional reserves for further development of known claims.",
    #     "Reserves for claims that may reopen in the future.",
    #     "Claims that have occurred but are not yet reported.",
    #     "Claims reported but not yet recorded in the system."
    # ]

    # # Create the circular chart
    # fig = go.Figure()

    # # Add the circular segments
    # for i, component in enumerate(components):
    #     fig.add_trace(go.Scatterpolar(
    #         r=[1, 1.2],  # Adjust this for visual consistency
    #         theta=[i * 360 / len(components), (i+1) * 360 / len(components)],
    #         fill='toself',
    #         name=component,
    #         hovertext=descriptions[i],
    #         mode='lines',
    #         line_color="rgba(0, 123, 255, 0.7)"  # Customize color as needed
    #     ))

    # # Configure the central point
    # fig.add_trace(go.Scatterpolar(
    #     r=[0],
    #     theta=[0],
    #     mode='markers+text',
    #     marker=dict(size=10, color="black"),
    #     text=["Claims Estimation Process"],
    #     textposition="top center"
    # ))

    # # Layout adjustments
    # fig.update_layout(
    #     polar=dict(
    #         radialaxis=dict(visible=False),
    #         angularaxis=dict(
    #             tickvals=[i * 360 / len(components) for i in range(len(components))],
    #             ticktext=components,
    #             rotation=90
    #         ),
    #     ),
    #     showlegend=False,
    #     title="Circular Infographic of Claims Estimation Components",
    #     width=600,  # Adjust size as needed
    #     height=600
    # )

    # # Display the chart in Streamlit
    # st.plotly_chart(fig)



    # Create a graphlib graph object
    # graph = graphviz.Digraph()
    # graph.edge("Components of Unpaid Claims", "Case Outstanding")
    # graph.edge("Components of Unpaid Claims", "Provision for Future Development on Known Claims")
    # graph.edge("Components of Unpaid Claims", "Estimate for Reopened Claims")
    # graph.edge("Components of Unpaid Claims", "Provision for IBNR")
    # graph.edge("Components of Unpaid Claims", "Provision for Claims in Transit")

    # st.graphviz_chart(graph)


    # Create a new directed graph
    # Create a new directed graph
    # graph = graphviz.Digraph()

    # # Set the graph attributes for color and layout
    # graph.attr(rankdir='TB', size='7,7')  # Top to bottom layout

    # # Add a central node with a distinct color and larger bold font
    # graph.node("Components of Unpaid Claims", 
    #         color='lightblue', 
    #         style='filled', 
    #         fontcolor='black', 
    #         shape='circle', 
    #         fontname='Helvetica-Bold')

    # # Define the components with colors and styles, increasing font size and bold
    # components = [
    #     ("Case Outstanding", "lightpink"),
    #     ("Provision for Future Development", "lightpink"),
    #     ("Estimate for Reopened Claims", "lightpink"),
    #     ("Provision for IBNR", "lightpink"),
    #     ("Provision for Claims in Transit", "lightpink")
    # ]

    # # Add nodes and edges for each component
    # for component, color in components:
    #     graph.node(component, 
    #             color=color, 
    #             style='filled', 
    #             fontcolor='black', 
    #             shape='circle', 
    #             fontname='Helvetica-Bold')  # Set the font to bold
    #     graph.edge("Components of Unpaid Claims", component)

    # # Render the graph in Streamlit
    # st.title("Components of Unpaid Claims")
    # st.graphviz_chart(graph)

    components = [
        "Case Outstanding",
        "Provision for Future Development",
        "Estimate for Reopened Claims",
        "Provision for IBNR",
        "Provision for Claims in Transit"
    ]

    # Define colors for each component
    colors = [
        "lightpink",
        "lightpink",
        "lightpink",
        "lightpink",
        "lightpink"
    ]

    # Calculate angles for positioning
    angles = np.linspace(0, 2 * np.pi, len(components), endpoint=False)

    # Create a Scatter plot
    fig = go.Figure()

    # Add the central node
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='text+markers',
        marker=dict(size=150, color='lightblue'),
        text=["Components of Unpaid Claims"],
        textposition="middle center",
        textfont=dict(size=18, color='white'),
        showlegend=False
    ))

    # Add each component node
    for angle, component, color in zip(angles, components, colors):
        x = np.cos(angle)  # X position on the circle
        y = np.sin(angle)  # Y position on the circle
        # Add a marker for each component
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers',
            marker=dict(size=75, color=color),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[0, x], y=[0, y],
            mode='lines+text',
            line=dict(color='lightpink'),
            text=[None, component],
            textposition="top center",
            textfont=dict(size=16, color='white'),
            showlegend=False
        ))

    fig.update_layout(
        title="Components of Unpaid Claims",
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=600,
        width=600
    )

    # Render the Plotly chart in Streamlit
    st.title("Components of Unpaid Claims")
    st.plotly_chart(fig)

    # Define nodes for the central concept and the five components
    # nodes = [
    #     Node(id="Components of Unpaid Claims", label="Components of Unpaid Claims", size=30),
    #     Node(id="Case Outstanding", label="Case Outstanding", size=20),
    #     Node(id="Provision for Future Development", label="Provision for Future Development", size=20),
    #     Node(id="Estimate for Reopened Claims", label="Estimate for Reopened Claims", size=20),
    #     Node(id="Provision for IBNR", label="Provision for IBNR", size=20),
    #     Node(id="Provision for Claims in Transit", label="Provision for Claims in Transit", size=20),
    # ]

    # # Create edges connecting each component to the central node
    # edges = [
    #     Edge(source="Components of Unpaid Claims", target="Case Outstanding"),
    #     Edge(source="Components of Unpaid Claims", target="Provision for Future Development"),
    #     Edge(source="Components of Unpaid Claims", target="Estimate for Reopened Claims"),
    #     Edge(source="Components of Unpaid Claims", target="Provision for IBNR"),
    #     Edge(source="Components of Unpaid Claims", target="Provision for Claims in Transit"),
    # ]

    # # Configure the layout and appearance of the graph
    # config = Config(
    #     width=750,
    #     height=750,
    #     directed=False,  # Set to False for an undirected graph
    #     physics=True,    # Enable physics for a more organic layout
    #     hierarchical=False  # Set to False for a circular layout
    # )

    # # Display the graph in Streamlit
    # st.title("Components of Unpaid Claims")
    # agraph(nodes=nodes, edges=edges, config=config)

    st.markdown("---")

    # Randomized Claims Transaction Table Example
    # st.subheader("Claims Transaction Table Example")
    # st.write("""
    # Below is an example of transactions related to a single claim, showing the progression over time. 
    # The table includes the type of transaction, amounts, and dates.
    # """)

    # # Generate example transactions for a single claim
    # transaction_types = ['Initial Estimate', 'Revised Estimate', 'Payment', 'Adjustment', 'Final Payment']
    # dates = pd.date_range(start='2023-01-01', periods=5, freq='Q')
    # amounts = np.random.randint(1000, 5000, size=5)

    # # Create a DataFrame for transactions
    # transactions = pd.DataFrame({
    #     'Transaction Type': transaction_types,
    #     'Date': dates,
    #     'Amount': amounts
    # })

    # st.table(transactions)
    st.markdown("**Policy Period:** December 1, 2007 to November 30, 2008  \n"
            "**Date of Accident:** November 15, 2008  \n"
            "**Date of Claim Report:** February 20, 2009")

    # Define the claim transactions data
    claim_data = {
        "Date": [
            "February 20, 2009",
            "April 1, 2009",
            "May 1, 2009",
            "September 1, 2009",
            "March 1, 2010",
            "January 25, 2011",
            "April 15, 2011",
            "September 1, 2011",
            "March 1, 2012"
        ],
        "Transaction": [
            "Case O/S of $15,000 established for claim only",
            "Claim payment of $1,500 – case O/S reduced to $13,500",
            "Expense payment to IA of $500 – no change in case O/S",
            "Case O/S for claim increased to $30,000",
            "Claim thought to be settled with additional payment of $24,000 – case O/S reduced to $0 and claim closed",
            "Claim reopened with case O/S of $10,000 for claim and $10,000 for defense costs",
            "Partial payment of $5,000 for defense litigation – no change in case O/S for claim",
            "Final claim payment for an additional $12,000 – case O/S for claim reduced to $0",
            "Final defense cost payment for an additional $6,000 – case O/S for defense costs reduced to $0 and claim closed"
        ],
        "Reported Value of Claim to Date": [
            "$15,000",
            "$15,000",
            "$15,500",
            "$32,000",
            "$26,000",
            "$46,000",
            "$46,000",
            "$48,000",
            "$49,000"
        ],
        "Cumulative Paid to Date": [
            "$0",
            "$1,500",
            "$2,000",
            "$2,000",
            "$26,000",
            "$26,000",
            "$31,000",
            "$43,000",
            "$49,000"
        ]
    }

# Create a DataFrame and display it
    claim_df = pd.DataFrame(claim_data)
    st.table(claim_df)
    st.markdown("---")

# Main App
def main():
    st.title("The Journey of a Claim")
    st.sidebar.title("Chapters")
    chapter = st.sidebar.radio("Go to:", ["Introduction", "Chapter 1: Understanding Reserves", 
                                          "Chapter 2: Claims Process and Estimation"])

    st.write("""
    This interactive app will guide you through the journey of a claim, from understanding reserves to the 
    complex estimation of unpaid claims. Let's dive into the details!
    """)

    if chapter == "Introduction":
        st.header("Introduction")
        st.write("""
        Insurance companies set aside reserves to ensure they can meet their claim obligations. Understanding how 
        these reserves are calculated and managed is essential for anyone studying insurance or working in the field.
        Use the sidebar to navigate between chapters.
        """)
    elif chapter == "Chapter 1: Understanding Reserves":
        chapter_1()
    elif chapter == "Chapter 2: Claims Process and Estimation":
        chapter_2()

if __name__ == "__main__":
    main()