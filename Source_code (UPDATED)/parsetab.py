
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASC AVG COMMA CONCATCOMMA CONCATSLASH CONCATSPACE CONST COUNT DESC DISTINCT EQ GROUP GT GTE ID ISNOTNULL ISNULL JOIN LEFTJOIN LPAREN LT LTE MAX MIN NEQ OR ORDER PROJECT RANK RPAREN SELECT SUM TABLE WINDOWexpression : TABLE\n                  | ORDER\n                  | DISTINCT\n                  | PROJECT\n                  | SELECT\n                  | GROUP\n                  | WINDOW\n                  | JOIN\n                  | LEFTJOINexpression : SELECT LPAREN table RPAREN LPAREN column_list RPARENtable : IDcolumn_list : ID COMMA ID\n                   | ID'
    
_lr_action_items = {'TABLE':([0,],[2,]),'ORDER':([0,],[3,]),'DISTINCT':([0,],[4,]),'PROJECT':([0,],[5,]),'SELECT':([0,],[6,]),'GROUP':([0,],[7,]),'WINDOW':([0,],[8,]),'JOIN':([0,],[9,]),'LEFTJOIN':([0,],[10,]),'$end':([1,2,3,4,5,6,7,8,9,10,18,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,]),'LPAREN':([6,14,],[11,15,]),'ID':([11,15,19,],[13,17,20,]),'RPAREN':([12,13,16,17,20,],[14,-11,18,-13,-12,]),'COMMA':([17,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'table':([11,],[12,]),'column_list':([15,],[16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> TABLE','expression',1,'p_expression','Algo2.py',68),
  ('expression -> ORDER','expression',1,'p_expression','Algo2.py',69),
  ('expression -> DISTINCT','expression',1,'p_expression','Algo2.py',70),
  ('expression -> PROJECT','expression',1,'p_expression','Algo2.py',71),
  ('expression -> SELECT','expression',1,'p_expression','Algo2.py',72),
  ('expression -> GROUP','expression',1,'p_expression','Algo2.py',73),
  ('expression -> WINDOW','expression',1,'p_expression','Algo2.py',74),
  ('expression -> JOIN','expression',1,'p_expression','Algo2.py',75),
  ('expression -> LEFTJOIN','expression',1,'p_expression','Algo2.py',76),
  ('expression -> SELECT LPAREN table RPAREN LPAREN column_list RPAREN','expression',7,'p_select_expression','Algo2.py',80),
  ('table -> ID','table',1,'p_table','Algo2.py',88),
  ('column_list -> ID COMMA ID','column_list',3,'p_column_list','Algo2.py',92),
  ('column_list -> ID','column_list',1,'p_column_list','Algo2.py',93),
]
