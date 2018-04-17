# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2017-04-20', 'CreateRule')

	def get_Select(self):
		return self.get_query_params().get('Select')

	def set_Select(self,Select):
		self.add_query_param('Select',Select)

	def get_RuleDesc(self):
		return self.get_query_params().get('RuleDesc')

	def set_RuleDesc(self,RuleDesc):
		self.add_query_param('RuleDesc',RuleDesc)

	def get_DataType(self):
		return self.get_query_params().get('DataType')

	def set_DataType(self,DataType):
		self.add_query_param('DataType',DataType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Where(self):
		return self.get_query_params().get('Where')

	def set_Where(self,Where):
		self.add_query_param('Where',Where)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_ShortTopic(self):
		return self.get_query_params().get('ShortTopic')

	def set_ShortTopic(self,ShortTopic):
		self.add_query_param('ShortTopic',ShortTopic)