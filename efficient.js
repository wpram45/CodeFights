  function roadchecker(adjacencyList,n)
{
    const atMostRoad=3
     let counter=0
     let found=false
    for(let i=0;i<n;i++)
    {
    
       
       for (let j=0;j<n;j++)
       {       
           
           //exclude it self
                if(i!==j)
                {
                    
                    found=false
                    
                
                    counter=1
                   
                         let neighbours=[...adjacencyList.get(i)]
                    while( neighbours.length>-1)
                    {
                          let neighbour;
                        counter+=1
                        
                                if(adjacencyList.get(i).includes(j))
                                {
                                        //console.log("direk bulundu i j",i,j)
                                        found=true
                                    
                                        break
                                        
                                }
                                    
                                else
                                {
                                    
                       
                    
                                
                                    if(neighbours.length>0)
                                    {
                                        neighbour=neighbours.pop()
                                        
                                        if(adjacencyList.get(neighbour).includes(j))
                                        {
                                            //console.log("komsudan bulundu","i neighbour j",i,neighbour,j)
                                            
                                            found=true
                                            break
                                        }
                                
                                        
                                    }
                                    
                                    else if(neighbours.length===0)
                                    {
                                        if (found!==true)
                                        {
                                            //console.log("bulunamadi i , j",i,j)
                                            
                                            return false
                                        }
                                    } 
                   
                        
                                 }  
                        
                    
                            
                        
                    }
            }
       }
    }
    
    return true
   
}


  
  
  
  
  const adjacencyList=new Map()

function addNode(city){
    
    adjacencyList.set(city,[])
    
}


function addEdge(from,to)
{
    
    adjacencyList.get(from).push(to)
    
}

function efficientRoadNetwork(n, roads) {
    
  //initalize empty adjaceny
  
  for(let cityNumber=0;cityNumber<n;cityNumber++){
      addNode(cityNumber)
  }
  

  
  
  for (const edge of roads)
  {
      
      addEdge(edge[0], edge[1])
      addEdge(edge[1], edge[0])
  }
    
    
   // console.log(adjacencyList)
    return roadchecker(adjacencyList, n)
   
      
      

}



    


