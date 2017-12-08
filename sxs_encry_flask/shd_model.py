#coding:utf-8
import sys
sys.path.append('D:\Python\shd_tools')
import tools

def get_auth(mobile):
	sxs_hehe = tools.sxs_db()
	#mobile='13801000010'
	authkey=sxs_hehe.get_data("SELECT authkey FROM vault_user_auth as a LEFT JOIN vault_user as u on a.user_id = u.id WHERE mobile = '%s'" % mobile)
	
	auth_id = authkey[0]['authkey'][14:21]
	return auth_id
	
print get_auth('13801000010')