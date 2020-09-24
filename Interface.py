

class SettingFunc(object):
	"""软件设置窗口SettingWindow"""
	def __init__(self, arg):
		super(SettingFunc, self).__init__()
		pass

	@classmethod
	def test_action(self, win):
		# 测试按钮点击事件 win : 设置窗口类
		pass

	@classmethod
	def unbound_machine_action(self, win):
		# 解绑机器按钮点击事件
		pass

class TaskFunc(object):
	"""软件任务窗口TaskWindow"""
	def __init__(self, arg):
		super(TaskFunc, self).__init__()
		pass

	@classmethod
	def start_action(self, win):
		# 开始所有任务按钮点击事件 win : 设置窗口类
		pass

	@classmethod
	def stop_action(self, win):
		# 停止所有按钮点击事件
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加任务窗口确认点击事件 win : 添加任务窗口类
		pass

	@classmethod
	def item_start_action(self, win):
		# 表格中开始任务按钮点击事件 win : QItem类
		pass

	@classmethod
	def item_copy_action(self, win):
		# 表格中复制按钮点击事件
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass

class AgentFunc(object):
	"""软件代理窗口AgentWindow"""
	def __init__(self, arg):
		super(AgentFunc, self).__init__()
		pass

	@classmethod
	def start_action(self, win):
		# 开始所有任务按钮点击事件 win : 设置窗口类
		pass

	@classmethod
	def stop_action(self, win):
		# 停止所有按钮点击事件
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加代理窗口确认点击事件 win : 添加代理窗口类
		pass

	@classmethod
	def ping_btn_action(self, win):
		# 添加代理窗口ping点击事件 win : 添加代理窗口类
		pass

	@classmethod
	def item_copy_action(self, win):
		# 表格中复制按钮点击事件 win : QItem类
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass


class AccountFunc(object):
	"""软件账号窗口AccountWindow"""
	def __init__(self, arg):
		super(AccountFunc, self).__init__()
		pass

	@classmethod
	def logging_action(self, win):
		# 登陆所有任务按钮点击事件 win : 设置窗口类
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加账号窗口确认点击事件 win : 添加账号窗口类
		pass

	@classmethod
	def item_start_action(self, win):
		# 表格中开始按钮点击事件 win : QItem类
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass


class DiscountFunc(object):
	"""软件折扣码窗口DiscountWindow"""
	def __init__(self, arg):
		super(DiscountFunc, self).__init__()
		pass

	@classmethod
	def select_action(self, win):
		# 查询所有任务按钮点击事件 win : 设置窗口类
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加折扣码窗口确认点击事件 win : 添加折扣码窗口类
		pass

	@classmethod
	def item_repeat_action(self, win):
		# 表格中重新开始按钮点击事件 win : QItem类
		print('re')
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass

class GiftFunc(object):
	"""软件礼品卡窗口GiftWindow"""
	def __init__(self, arg):
		super(GiftFunc, self).__init__()
		pass

	@classmethod
	def select_action(self, win):
		# 查询所有任务按钮点击事件 win : 礼品卡窗口类
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加礼品卡窗口确认点击事件 win : 添加礼品卡窗口类
		pass

	@classmethod
	def item_repeat_action(self, win):
		# 表格中重新开始按钮点击事件 win : QItem类
		print('gift')
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass



class AddressFunc(object):
	"""软件地址窗口AddressWindow"""
	def __init__(self, arg):
		super(AddressFunc, self).__init__()
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass

	@classmethod
	def confirm_btn_action(self, win):
		# 添加地址窗口确认点击事件 win : 添加地址窗口类
		pass

	@classmethod
	def item_copy_action(self, win):
		# 表格中复制按钮点击事件 win : QItem类
		pass

	@classmethod
	def item_delete_action(self, win):
		# 表格中删除按钮点击事件
		pass

class OrderFunc(object):
	"""软件订单窗口OrderWindow"""
	def __init__(self, arg):
		super(OrderFunc, self).__init__()
		pass

	@classmethod
	def export_action(self, win):
		# 导出所有任务按钮点击事件 win : 订单窗口类
		pass

	@classmethod
	def delete_action(self, win):
		# 删除所有按钮点击事件
		pass