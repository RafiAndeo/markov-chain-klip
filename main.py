import graphviz

states = ["Start", "v_Home_Page", "v_Login_Page", "v_Register_Page", "v_Dashboard_User_Page", "v_Dashboard_Admin_Page", "v_Product_Details_Page",
          "v_Cart_Page", "v_Success_Checkout_Page", "v_My_Transaction_Page", "v_Show_My_Transaction_Page", "v_Dashboard_Admin_Product_Page",
          "v_Create_Product_Page", "v_Gallery_Product_Page", "v_Upload_Photos_Page", "v_Edit_Product_Page", "v_Dashboard_Admin_Transaction_Page",
          "v_Show_Transaction_Page", "v_Edit_Transaction_Page", "v_Dashboard_Admin_User_Page", "v_Edit_User_Page", "End"]

transition_probs = {
    "Start": {"v_Home_Page": 1.0},
    "v_Home_Page": {"v_Login_Page": 0.3, "v_Register_Page": 0.3, "v_Product_Details_Page": 0.2, "v_Cart_Page": 0.2},
    "v_Login_Page": {"v_Dashboard_User_Page": 0.8, "v_Dashboard_Admin_Page": 0.2},
    "v_Register_Page": {"v_Dashboard_User_Page": 1.0},
    "v_Dashboard_User_Page": {"v_Home_Page": 0.6, "v_My_Transaction_Page": 0.4},
    "v_Dashboard_Admin_Page": {"v_Home_Page": 0.6, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "v_My_Transaction_Page": 0.1},
    "v_Product_Details_Page": {"v_Home_Page": 0.5, "v_Cart_Page": 0.3, "v_Dashboard_User_Page": 0.1, "v_Dashboard_Admin_Page": 0.1},
    "v_Cart_Page": {"v_Home_Page": 0.3, "v_Success_Checkout_Page": 0.5, "v_Dashboard_User_Page": 0.1, "v_Dashboard_Admin_Page": 0.1},
    "v_Success_Checkout_Page": {"v_Home_Page": 0.3, "v_Cart_Page": 0.1, "v_Dashboard_User_Page": 0.3, "v_Dashboard_Admin_Page": 0.3},
    "v_My_Transaction_Page": {"v_Dashboard_User_Page": 0.1, "v_Show_My_Transaction_Page": 0.2, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.3},
    "v_Show_My_Transaction_Page": {"v_My_Transaction_Page": 0.1, "v_Dashboard_User_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.4},
    "v_Dashboard_Admin_Product_Page": {"v_Dashboard_Admin_Page": 0.1, "v_My_Transaction_Page": 0.1, "v_Create_Product_Page": 0.2, "v_Gallery_Product_Page": 0.2, "v_Edit_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Create_Product_Page": {"v_Dashboard_Admin_Product_Page": 0.5, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Gallery_Product_Page": {"v_Dashboard_Admin_Product_Page": 0.1, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "Upload_Photos_Page": 0.5, "End": 0.1},
    "v_Upload_Photos_Page": {"v_Gallery_Product_Page": 0.4, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Edit_Product_Page": {"v_Dashboard_Admin_Product_Page": 0.5, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Dashboard_Admin_Transaction_Page": {"v_Dashboard_Admin_Page": 0.1, "v_My_Transaction_Page": 0.1, "v_Show_Transaction_Page": 0.2, "v_Edit_Transaction_Page": 0.3, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Show_Transaction_Page": {"v_Dashboard_Admin_Transaction_Page": 0.1, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.5},
    "v_Edit_Transaction_Page": {"v_Dashboard_Admin_Transaction_Page": 0.5, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_User_Page": 0.1, "End": 0.1},
    "v_Dashboard_Admin_User_Page": {"v_Dashboard_Admin_Page": 0.1, "v_My_Transaction_Page": 0.1, "v_Edit_User_Page": 0.5, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "End": 0.1},
    "v_Edit_User_Page": {"v_Dashboard_Admin_User_Page": 0.5, "v_My_Transaction_Page": 0.1, "v_Dashboard_Admin_Page": 0.1, "v_Dashboard_Admin_Product_Page": 0.1, "v_Dashboard_Admin_Transaction_Page": 0.1, "End": 0.1},
    "End": {"End": 1.0}
}

dot = graphviz.Digraph(comment="Klip Application Markov Chain Model")
for state in states:
    dot.node(state)
for state, next_states in transition_probs.items():
    for next_state, prob in next_states.items():
        dot.edge(state, next_state, label=str(prob))
dot.render("klip_model.gv", view=True)
