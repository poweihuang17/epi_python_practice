import collections

WHITE, BLACK = range(2)
Coordinate= collections.namedtuple('Coordinate', ('x', 'y') )


def search_maze( maze, s, e):
	
	#Perform DFS to find a feasible path
	def search_maze_helper(cur):

		if not ( 0<=cur.x< len(maze) and 0<=cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE ):
			return False

		path.append(cur)
		
		#This is strange. Shouldn't we put it back into white later?
		#No, because it could reduce redundancy.
		maze[cur.x][cur.y]=BLACK

		if cur == e:
			#print path
			return True

		if any( map(search_maze_helper, ( Coordinate(cur.x-1,cur.y), Coordinate(cur.x+1,cur.y), Coordinate(cur.x,cur.y-1), Coordinate(cur.x,cur.y+1) )) ):
			return True

		#Cannot find a path, remove the latest path.
		del path[-1]
		return False




	path=[]
	if not search_maze_helper(s):
		return [] # No path between s and e

	return path

maze=[[BLACK,WHITE,WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, WHITE, WHITE], [WHITE,WHITE, BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE], [BLACK,WHITE,BLACK,WHITE,WHITE,BLACK,BLACK,WHITE,BLACK,BLACK],[WHITE,WHITE,WHITE,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,WHITE],[WHITE,BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE],[WHITE,BLACK,BLACK,WHITE,WHITE,BLACK,WHITE,BLACK,BLACK,WHITE],[WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE],[BLACK,WHITE,BLACK,WHITE,BLACK,WHITE,BLACK,WHITE,WHITE,WHITE],[BLACK,WHITE,BLACK,BLACK,WHITE,WHITE,WHITE,BLACK,BLACK,BLACK],[WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,BLACK,WHITE]]
for x in maze:
	s=''
	for y in x:
		if y is BLACK:
			s+='X'
		else:
			s+='O'
	print s

print search_maze( maze, Coordinate(9,0), Coordinate(0,9))

