class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.headval = None

    def __iter__(self):
        node = self.headval
        while node:
            yield node
            node = node.next

    def get(self, index: int) -> int:
        getval = self.headval
        count = 0
        val = -1
        while getval != None:
            if count == index:
                val = getval.dataval
                return val
            getval = getval.next
            count+=1

        


        return val
            

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if self.headval == None:
            self.headval = temp
        else:
            temp.next = self.headval
            self.headval = temp
        print(self.headval.dataval)
            
        

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.headval == None:
            self.headval = temp
            return
        lastval = self.headval
        while(lastval.next):
            lastval = lastval.next
        lastval.next = temp



    def addAtIndex(self, index: int, val: int) -> None:
        temp = Node(val)
        if self.headval == None:
            self.headval = temp
            return
        indexval = self.headval
        count = 0 
        while indexval.next:
            if count== index-1:
                temp.next = indexval.next
                indexval.next = temp
                return
            indexval = indexval.next
            count+=1
        if indexval.next == None and count is index-1:
            self.addAtTail(val)
        if index == 0:
            self.addAtHead(val)
        
    def deleteAtIndex(self, index: int) -> None:
        indexval = self.headval
        count = 0 
        temp = indexval

        while indexval.next:
            # check if index to delete at
            # set previous node next val to current node next val
            if count == index:
                if count == 0:
                    self.headval = temp.next
                    return
                temp.next = indexval.next
                return
            count+=1
            temp = indexval
            indexval = indexval.next
        if index is count:
            temp.next = None



    def listprint(self):
      printval = self.headval
      while printval != None:
         print (printval.dataval)
         printval = printval.next
        

myLinkedList = MyLinkedList()

values = [[70],[1],[1],[1],[857],[1],[761],[32],[2,725],[195],[3],[69],[1],[905],[649],[2,239],[183],[775],[8,286],[3],[593],[2,196],[10,716],[5],[129],[702],[797],[2],[14],[9,758],[541],[337],[211],[476],[18,732],[620],[509],[13,93],[12],[366],[194],[886],[12,594],[5],[607],[825],[26,970],[471],[337],[427],[774],[10,235],[964],[494],[139],[960],[12,699],[30],[285],[11],[741],[349],[293],[31,993],[44,800],[247],[43],[38,537],[125],[251],[36,703],[27],[29,657],[734],[541],[363],[35],[33],[537],[25],[14],[44],[6],[36],[9,224],[32],[837],[9],[952],[771],[27,982],[50,68],[853],[13,465],[994],[788],[345],[186],[47],[254],[53],[54,310],[745],[129],[429],[26],[7,83],[857],[52],[323],[488],[24],[792],[56],[203],[623],[1],[35,836],[13],[556],[756],[17],[675],[529],[70],[14],[466],[44],[50],[38],[14],[364],[840],[14],[55,753],[47],[969],[832],[442],[17],[3],[28],[75,756],[777],[419],[376],[43],[891],[24,866],[13],[67],[614],[522],[393],[61],[350],[808],[83,302],[7],[761],[299],[67],[93],[657],[540],[82,499],[55],[686],[240],[93],[911],[98],[61],[560],[86],[20],[77],[943],[949],[18,694],[622],[96],[32],[693],[401],[554],[620],[53],[501],[1,221],[749],[84],[722],[143],[918],[55],[33,116],[218],[691],[12],[136],[381],[184],[53,208],[6,291],[574],[43],[616],[726],[123],[499],[48,932],[63],[822],[124],[12],[108,276],[92],[283],[85],[100],[91,468],[36],[488],[165],[699],[111,847],[685],[601],[325],[931],[881],[760],[68],[109,520],[390],[454],[164],[70],[364],[905],[6],[110],[398],[65,557],[251],[142],[126],[144],[995],[55,398],[61],[432],[67],[136,188],[106],[847],[10,625],[46],[143,38],[81],[104],[111,804],[388],[540],[396],[13,933],[826],[26],[367],[42],[700],[43],[17,989],[114],[55],[498],[162],[651],[116],[118],[293],[126],[128],[265],[395],[0],[900],[163],[686],[974],[37,185],[78,321],[938],[423],[880],[114],[118,367],[28],[5],[263],[133,878],[701],[158],[433],[59],[149],[896],[434],[30],[515],[38],[864],[441],[389],[443],[113],[912],[537],[442],[574],[890],[476],[455],[782],[170,175],[969],[957],[452],[154,828],[264],[13],[146,196],[583],[673],[535],[968],[100],[155],[597],[109],[516],[61],[793],[517],[86,498],[130,838],[737],[245],[93,72],[189],[36],[2],[856],[749],[75,479],[368],[598],[734],[340],[179,573],[28],[271],[215],[174],[379],[304],[525],[985],[222,767],[27,362],[55],[87,404],[558],[544],[33,88],[351],[155],[168],[170,814],[92],[354],[108],[17,63],[535],[4],[704],[345],[299],[340],[4,358],[522],[783],[231],[400],[282],[921],[466],[708],[5],[146],[613],[883],[655],[839],[96],[714],[489],[954],[23],[32,872],[174],[107,92],[198],[28],[228,51],[212],[102,90],[281],[813],[32,649],[667],[299],[349],[800],[749],[611],[183],[44],[530],[209],[993],[440],[148],[354],[265],[906],[46,788],[924],[684],[200,102],[73],[667],[205,287],[687],[157],[398],[254],[264],[582],[81],[213],[8],[569],[33,117],[31],[108],[48],[4],[102],[128,148],[726],[122],[45],[34],[680],[284],[243],[726],[251,375],[138],[514],[125],[33],[216,560],[147],[808],[933],[980],[546],[460],[208],[412],[93,465],[795],[294],[84,894],[171],[593],[968],[64],[178],[39,388],[832],[105,742],[471],[758],[113],[564],[633],[608],[151,886],[12,5],[415],[241,525],[90],[150],[423],[892],[201],[890],[384],[133,519],[305],[149],[303,67],[907],[79],[27],[116],[38],[722],[253,307],[670],[85],[463],[126],[281,656],[295],[200],[25],[407],[323],[7],[812],[545],[60,583],[15],[743],[333],[637],[120,851],[22],[923],[137],[304],[31],[378],[323],[798],[292],[799],[23,303],[318],[30],[80],[335],[94],[607],[668],[167],[229],[84,446],[53,308],[934],[160],[691],[654],[988],[265],[700],[462],[0],[244,275],[659],[603],[4],[930],[64,338],[382],[987],[800],[324],[264],[29],[410],[102],[916],[943],[29,480],[186],[180],[291],[101],[142],[197],[283],[335,984],[380,756],[116],[796],[712],[421],[404],[832],[944],[158],[92],[1],[228],[98],[78],[919],[991],[31],[740],[975],[241,330],[739],[280],[595],[60],[988],[716],[819],[109],[30],[919],[69],[207],[201],[25],[130],[77],[186],[805],[377],[4],[47,421],[406],[285],[419],[985],[671],[758],[315],[367],[56,195],[851],[41],[403,902],[179],[416],[14],[412],[2],[90],[497],[136],[984],[344],[600],[239,234],[158],[197],[119,147],[279],[878],[906],[407],[898],[111,826],[632],[567],[718],[243],[304],[60],[27],[554],[134,838],[177],[255,989],[116],[998],[192],[34],[92],[858],[490],[9],[350],[571],[412,362],[520],[384,886],[425],[44],[320],[985],[842],[271],[212],[405],[706],[482],[28],[416],[660],[264],[979],[105,755],[360],[145],[240,539],[209],[452,989],[640],[425],[249],[123],[811],[758],[186],[389],[442],[664],[210,447],[303],[288],[283],[465],[999],[441,501],[407],[273],[517],[60],[297,358],[159],[398,212],[767],[340,139],[178],[954],[151],[481],[32],[579],[70],[466],[466],[934],[102],[801],[41],[220,271],[141,76],[14,956],[170],[895],[478],[179],[235,524],[61],[148,96],[47,25],[727],[978],[169],[407],[418,24],[407],[333],[719],[251],[162,183],[804],[350,245],[652],[544],[687],[989],[59],[169],[922],[595],[994],[212],[119],[383],[225],[308,491],[318],[37],[487],[287,965],[149],[98],[700],[991],[15,254],[151],[444],[640],[320],[165],[507,510],[228],[240,319],[656],[64],[397],[220],[263],[793],[299],[905],[319],[892],[304,955],[566],[273,749],[145,948],[554],[739],[289],[366],[308],[694],[423],[767],[213],[388],[219],[408],[45],[398],[337,120],[210],[406,12],[458],[359],[50],[765],[432],[25],[121],[220,641],[389],[962],[597],[196],[453],[33],[448,113],[414],[118,146],[292],[126,138],[467],[479],[543],[91],[923],[60],[453],[210],[141],[278],[208],[449],[437,848],[219],[182],[336,147],[11],[967],[37],[256],[184],[654],[189,183],[76,378],[432],[425],[731],[467],[345,340],[30],[185],[245,438],[674],[78],[96],[440,101],[642],[520],[976],[243],[930],[114],[799],[514],[118],[153,70],[171,555],[887],[270,736],[831],[769],[694],[204,426],[612],[660],[70],[132],[68,165],[611],[995],[248,24],[496],[594],[444,272],[346],[647],[892],[165],[77],[279],[274],[81],[74],[43,816],[452,341],[12],[667],[718],[942],[153,51],[322,130],[428],[370],[790],[457],[34],[1],[139],[84],[265,712],[844],[382],[111,72],[565],[797],[730],[898],[357,651],[166],[334],[275],[580],[137],[532],[212],[463,567],[313],[700],[264],[29],[976],[43],[131],[404],[864],[9],[508],[523,906],[884],[388,204],[556],[177,621],[527],[494],[627],[80],[131],[261,652],[644],[810],[246],[155],[695],[131],[511],[655],[963],[253],[600,932],[209],[471]]
commands = ["addAtHead","deleteAtIndex","get","deleteAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtTail","addAtIndex","addAtHead","get","addAtTail","get","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtIndex","get","addAtHead","addAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","get","get","addAtIndex","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","addAtIndex","get","addAtTail","addAtTail","addAtHead","addAtIndex","get","addAtHead","addAtHead","addAtIndex","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","addAtTail","addAtIndex","get","addAtHead","get","addAtHead","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtTail","get","addAtIndex","addAtHead","addAtHead","addAtIndex","get","addAtIndex","addAtTail","addAtHead","addAtHead","get","get","addAtHead","deleteAtIndex","deleteAtIndex","get","get","deleteAtIndex","addAtIndex","addAtTail","addAtTail","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtTail","addAtIndex","addAtTail","addAtTail","addAtHead","addAtHead","get","addAtTail","get","addAtIndex","addAtTail","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtTail","get","addAtHead","addAtTail","get","addAtIndex","deleteAtIndex","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtTail","get","get","addAtHead","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtHead","get","deleteAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtTail","addAtTail","get","addAtHead","addAtIndex","get","get","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtIndex","deleteAtIndex","addAtTail","addAtTail","get","get","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","deleteAtIndex","addAtHead","addAtTail","deleteAtIndex","get","get","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","addAtTail","addAtTail","addAtHead","deleteAtIndex","addAtHead","addAtIndex","addAtHead","get","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtIndex","addAtTail","addAtTail","get","addAtTail","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtTail","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","get","addAtHead","deleteAtIndex","deleteAtIndex","addAtIndex","get","addAtHead","get","deleteAtIndex","addAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtTail","addAtIndex","addAtHead","deleteAtIndex","get","addAtTail","addAtTail","addAtIndex","get","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtHead","addAtIndex","get","addAtIndex","get","deleteAtIndex","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtTail","get","addAtIndex","get","get","addAtHead","get","addAtHead","get","get","addAtTail","get","get","addAtTail","addAtHead","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtIndex","addAtTail","get","addAtTail","addAtIndex","addAtTail","get","addAtHead","get","deleteAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtHead","addAtTail","addAtHead","addAtHead","addAtTail","addAtIndex","addAtTail","addAtHead","addAtTail","addAtIndex","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","get","deleteAtIndex","addAtTail","get","addAtHead","get","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","deleteAtIndex","get","addAtHead","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","addAtIndex","addAtHead","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","get","addAtIndex","addAtHead","addAtHead","addAtHead","addAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtTail","addAtTail","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtHead","addAtIndex","get","addAtTail","addAtIndex","get","addAtIndex","addAtHead","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtHead","addAtTail","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtTail","addAtHead","deleteAtIndex","addAtTail","get","addAtTail","addAtIndex","addAtTail","addAtHead","addAtIndex","get","addAtHead","addAtIndex","addAtHead","deleteAtIndex","addAtHead","addAtHead","get","addAtHead","deleteAtIndex","addAtHead","deleteAtIndex","addAtHead","addAtIndex","deleteAtIndex","get","deleteAtIndex","get","deleteAtIndex","addAtIndex","addAtTail","addAtTail","get","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtIndex","get","addAtHead","addAtTail","addAtHead","addAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","addAtHead","addAtHead","addAtIndex","addAtHead","get","addAtIndex","deleteAtIndex","addAtTail","addAtTail","get","addAtTail","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","get","get","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtTail","deleteAtIndex","addAtIndex","get","deleteAtIndex","deleteAtIndex","addAtTail","get","get","addAtTail","addAtTail","addAtIndex","get","addAtTail","addAtTail","addAtHead","addAtIndex","addAtTail","addAtHead","deleteAtIndex","addAtTail","get","addAtHead","addAtTail","addAtTail","get","addAtTail","addAtIndex","addAtHead","addAtTail","get","addAtHead","addAtTail","addAtTail","addAtTail","get","get","addAtIndex","addAtIndex","addAtTail","addAtTail","addAtHead","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtTail","addAtTail","get","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","get","addAtTail","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtIndex","get","get","addAtHead","get","get","deleteAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtHead","get","get","addAtTail","get","addAtTail","get","addAtHead","addAtHead","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","deleteAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtIndex","addAtHead","get","addAtIndex","addAtHead","get","addAtTail","addAtTail","addAtHead","get","addAtHead","addAtHead","addAtHead","addAtTail","addAtHead","addAtIndex","get","get","addAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","deleteAtIndex","get","deleteAtIndex","addAtTail","addAtTail","addAtIndex","get","addAtIndex","addAtTail","addAtHead","addAtHead","deleteAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtHead","deleteAtIndex","addAtHead","addAtIndex","addAtHead","addAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtTail","addAtTail","get","get","addAtHead","addAtHead","addAtTail","addAtIndex","get","get","addAtIndex","addAtHead","addAtIndex","addAtHead","get","addAtHead","deleteAtIndex","addAtTail","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","deleteAtIndex","addAtTail","deleteAtIndex","addAtHead","addAtIndex","addAtHead","addAtHead","addAtHead","addAtTail","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtIndex","addAtTail","addAtHead","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtTail","addAtHead","get","addAtTail","deleteAtIndex","addAtIndex","addAtIndex","addAtIndex","addAtHead","addAtTail","get","deleteAtIndex","addAtIndex","addAtTail","addAtIndex","addAtIndex","addAtTail","addAtTail","addAtTail","get","addAtIndex","get","deleteAtIndex","addAtTail","get","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","addAtHead","get","addAtTail","addAtTail","addAtHead","addAtHead","get","addAtHead","deleteAtIndex","get","addAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtIndex","addAtTail","get","addAtTail","get","addAtHead","addAtTail","deleteAtIndex","addAtHead","deleteAtIndex","addAtTail","addAtIndex","addAtHead","addAtIndex","addAtIndex","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","get","addAtHead","deleteAtIndex","get","deleteAtIndex","get","deleteAtIndex","addAtTail","addAtIndex","addAtTail","addAtIndex","get","addAtTail","get","addAtTail","deleteAtIndex","get","get","addAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtIndex","deleteAtIndex","deleteAtIndex","addAtTail","get","addAtTail","addAtTail","get","addAtTail","get","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","get","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtTail","get","addAtIndex","addAtHead","get","addAtHead","addAtHead","addAtHead","addAtTail","addAtHead","addAtHead","deleteAtIndex","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtHead","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","deleteAtIndex","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","deleteAtIndex","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtTail","get","addAtHead","get","addAtHead","get","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtHead","get","addAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtTail","deleteAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtIndex","get","addAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","addAtHead","addAtHead","deleteAtIndex","addAtTail","addAtHead","addAtHead","deleteAtIndex","addAtHead","addAtTail","get","addAtIndex","get","get"]
count = 0

for command in commands:
    value = values[count]
    if len(value) > 1:
        class_method = getattr(myLinkedList, command)
        class_method(value[0],value[1])
    else:
        class_method = getattr(myLinkedList, command)
        class_method(value[0])

    count+=1

print([node.dataval for node in myLinkedList] )
