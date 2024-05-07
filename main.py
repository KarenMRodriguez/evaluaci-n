import modules.corefiles as cf
import funciones.globales as gf
import ui.uiProductos as uiP

def mainMenu(op):
    gf.borrar_pantalla()
    title= """
    *****************
    ** MENU TIENDA **
    *****************
    """
    mainMenuOp= "1.registrar productos/n2.salir"

    if(op !=2):
       print(title)
       print(mainMenuOp)
    try:
        opcion=int(input(':)'))
    except ValueError:
        print("opcion no valida")
        gf.pausar_pantalla()
        mainMenu()

    else:
       match(opcion):
        case 1:
           uiP.menuProductos(0)
        case _:
           print()
           gf.pausar_pantalla

           mainMenu()

if __name__=='__main__':
   cf.MY_DATABASE="data/productos.json"
   cf.checkFile(gf.Tienda)
   mainMenu(0)                
           
           
          
         
            


    
    
     
    
 
              
       
       
       
    
    
      
                 
                     
              
    
       
    
    
        

                
               





