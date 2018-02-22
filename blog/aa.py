# -*- coding: UTF-8 -*-
def formula_lgw_risk_opereate(reg_status,seed,manager_change_num1y,address_change_num2y,stock_change_num6m,stock_change_num2y,name_change_num2y,scope_change_num2y,type_change_num2y,year_score,job_sum_score,stock_score,stock_sum_score,inst_sum_score,time_change_score,reg_k_change_score,stake_change_score,stock_mortgage_score,cross_score,reg_k):
      #from _future_ import division
  if reg_status is not 1:
    return 99 - seed
  if manager_change_num1y > 1 or address_change_num2y > 1 or stock_change_num6m > 3 or stock_change_num2y > 3 or name_change_num2y > 1 or scope_change_num2y > 1 or type_change_num2y > 1:
    return 100 - (480+seed/2-300)/550.0*100
  operate_score = year_score + job_sum_score + stock_score + stock_sum_score + inst_sum_score + time_change_score + reg_k_change_score + stake_change_score + stock_mortgage_score + cross_score
  if reg_k < 1000:
    operate_score = 100-(operate_score-1*5+229)/(220+229.0)* 100
  else:
    operate_score = 100-(operate_score- 1*5+246)/(210+246.0)*100
  if operate_score > 99:
    return 99
  if operate_score < 5:
    return 5
  return operate_score

def formula_stock_num(relevance_shareholders):
  params = relevance_shareholders
  return len(params.get('investors',[]))

def formula_inst_num(relevance_shareholders):
  investors = relevance_shareholders.get('investors',[])
  num = 0
  for investor in investors:
    if investor.get('is_company', 0) is 1:
      num += 1
  return num

shareholders = '''{
        "company": "上海冰鉴信息科技有限公司",
        "uuid": "d7d7d0ae35be3323b40b42ed73f97a0a",
        "date": "2018-02-19 01:27:55",
        "investors": [
            {
                "company": "宁波创世一期股权投资基金合伙企业（有限合伙）",
                "uuid": "01c19ae560263c0eb29f60bfebe5d96e",
                "name": "宁波创世一期股权投资基金合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海峰瑞创业投资中心（有限合伙）",
                "uuid": "227945b8d6193913ab38b2dc6b7c99e7",
                "name": "上海峰瑞创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "uuid": "3fd9071cfcf03da7805db80f99177ebd",
                "name": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海峰瑞投资中心（有限合伙）",
                "uuid": "4ac102009511310280d00fa945f82e1d",
                "name": "上海峰瑞投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "杭州挖财互联网金融服务有限公司",
                "uuid": "6045a62e04ad361e9b7dc0dc5503090d",
                "name": "杭州挖财互联网金融服务有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海冰鉴文化传播合伙企业（有限合伙）",
                "uuid": "80f01156307837aa96501bcc0fa2e2da",
                "name": "上海冰鉴文化传播合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "百咖（上海）创业投资中心（有限合伙）",
                "uuid": "90cc435bf41c3988ac3d22f867c84d77",
                "name": "百咖（上海）创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海唯猎创业投资中心（有限合伙）",
                "uuid": "a2b85d1b102232f3bc93fc2e02e6988d",
                "name": "上海唯猎创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "北京华阳金辰企业管理中心（有限合伙）",
                "uuid": "b5e8940fcf603d2e895a0fb7460fe1ad",
                "name": "北京华阳金辰企业管理中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海微特融优投资管理合伙企业（有限合伙）",
                "uuid": "b6cd0ce3e10a3bc4bfcdbdfae864009a",
                "name": "上海微特融优投资管理合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "南京本立道生数据科技有限公司",
                "uuid": "bab9a861cb5431a4b63a2e3581e6c8c3",
                "name": "南京本立道生数据科技有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "北京德辉投资发展有限公司",
                "uuid": "be8620e95c8f3dcb888a7ba9e33dcd8e",
                "name": "北京德辉投资发展有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "杭州云驰创业投资合伙企业（有限合伙）",
                "uuid": "cc2c500db5d63f72b925228eb002d2d9",
                "name": "杭州云驰创业投资合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "uuid": "12f40ebdb6713b3094ebdfbbf1bead8d",
                "name": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "上海唯猎创业投资中心（有限合伙）",
                "uuid": "2520cb984cf439fda62bf5f1aa8fc50e",
                "name": "上海唯猎创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "百咖（上海）创业投资中心（有限合伙）",
                "uuid": "a8d4371e1926310b8eed6198ead64621",
                "name": "百咖（上海）创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "上海峰瑞投资中心（有限合伙）",
                "uuid": "ecfadcc696fe32cfa565cc567b609f4e",
                "name": "上海峰瑞投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            }
        ],
        "ent_shareholders": [
            {
                "company": "宁波创世一期股权投资基金合伙企业（有限合伙）",
                "uuid": "01c19ae560263c0eb29f60bfebe5d96e",
                "name": "宁波创世一期股权投资基金合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海峰瑞创业投资中心（有限合伙）",
                "uuid": "227945b8d6193913ab38b2dc6b7c99e7",
                "name": "上海峰瑞创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "uuid": "3fd9071cfcf03da7805db80f99177ebd",
                "name": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海峰瑞投资中心（有限合伙）",
                "uuid": "4ac102009511310280d00fa945f82e1d",
                "name": "上海峰瑞投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "杭州挖财互联网金融服务有限公司",
                "uuid": "6045a62e04ad361e9b7dc0dc5503090d",
                "name": "杭州挖财互联网金融服务有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海冰鉴文化传播合伙企业（有限合伙）",
                "uuid": "80f01156307837aa96501bcc0fa2e2da",
                "name": "上海冰鉴文化传播合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "百咖（上海）创业投资中心（有限合伙）",
                "uuid": "90cc435bf41c3988ac3d22f867c84d77",
                "name": "百咖（上海）创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海唯猎创业投资中心（有限合伙）",
                "uuid": "a2b85d1b102232f3bc93fc2e02e6988d",
                "name": "上海唯猎创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "北京华阳金辰企业管理中心（有限合伙）",
                "uuid": "b5e8940fcf603d2e895a0fb7460fe1ad",
                "name": "北京华阳金辰企业管理中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "上海微特融优投资管理合伙企业（有限合伙）",
                "uuid": "b6cd0ce3e10a3bc4bfcdbdfae864009a",
                "name": "上海微特融优投资管理合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "南京本立道生数据科技有限公司",
                "uuid": "bab9a861cb5431a4b63a2e3581e6c8c3",
                "name": "南京本立道生数据科技有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "北京德辉投资发展有限公司",
                "uuid": "be8620e95c8f3dcb888a7ba9e33dcd8e",
                "name": "北京德辉投资发展有限公司",
                "investment": 0,
                "shareholder_type": "企业法人",
                "date": "-",
                "is_company": 1
            },
            {
                "company": "杭州云驰创业投资合伙企业（有限合伙）",
                "uuid": "cc2c500db5d63f72b925228eb002d2d9",
                "name": "杭州云驰创业投资合伙企业（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 1
            }
        ],
        "per_shareholders": [
            {
                "company": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "uuid": "12f40ebdb6713b3094ebdfbbf1bead8d",
                "name": "西藏领沨鑫服创业投资合伙协议（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "上海唯猎创业投资中心（有限合伙）",
                "uuid": "2520cb984cf439fda62bf5f1aa8fc50e",
                "name": "上海唯猎创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "百咖（上海）创业投资中心（有限合伙）",
                "uuid": "a8d4371e1926310b8eed6198ead64621",
                "name": "百咖（上海）创业投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            },
            {
                "company": "上海峰瑞投资中心（有限合伙）",
                "uuid": "ecfadcc696fe32cfa565cc567b609f4e",
                "name": "上海峰瑞投资中心（有限合伙）",
                "investment": 0,
                "shareholder_type": "合伙企业",
                "date": "-",
                "is_company": 0
            }
        ]
    }'''

import json
shareholders = json.loads(shareholders, encoding='UTF-8')
print formula_inst_num(shareholders)
print formula_stock_num(shareholders)