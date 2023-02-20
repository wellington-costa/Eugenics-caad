
"""

MDBoxLayout:
            md_bg_color: 0/255, 0/255, 150/255, 1
            size_hint_y:.08
            size_hint_x:1
            pos_hint:{"center_x":.5,"center_y":.86}
            padding:20
            orientation:"horizontal"
            MDLabel:
                text:"Cadastro de Membro"
                #adaptive_size:True
                halign:"center"
        MDBoxLayout:
                md_bg_color: 200/255, 200/255, 255/255, 1
                size_hint_y:.75
                size_hint_x:.9
                pos_hint:{"center_x":.5,"center_y":.44}
                padding:20
                orientation:"vertical"
                MDTextField:
                    id: nome
                    hint_text:"Nome Completo:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.75}
                MDTextField:
                    id: cpf
                    hint_text:"CPF:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}

                MDTextField:
                    id: data_nasc
                    hint_text:"Data de Nascimento"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}
                    on_focus: root.showDatePicker()

                MDTextField:
                    id: data_membro
                    hint_text:"Membro desde:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}
                    #on_focus: root.showDatePicker()

                MDTextField:
                    id: endereco
                    hint_text:"Endereço:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}

                MDTextField:
                    id: congregacao
                    hint_text:"Congregaçao:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}

                MDTextField:
                    id: departamento
                    hint_text:"Departamento:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}

                MDTextField:
                    id: cargo
                    hint_text:"Cargo:"
                    size_hint_x:.9
                    #pos_hint:{"center_x":.5, "center_y":.9}
                MDBoxLayout:
                    orientation:"horizontal"
                    md_bg_color: 200/255, 200/255, 200/255, 1
                    size_hint_x:1
                    MDRaisedButton:
                        text: "Cancelar"

                    MDLabel:
                        text:""
                    MDRaisedButton:
                        text:"Salvar"
                        pos_hint_x:
"""