# 巡检包及台账格式

packet_preview 当前只保存投递、校验任务并转换已知字段，不做跨包合流，也不会自动进入正式台账。
ZIP 中 manifest.json 唯一；附件以 photo_id 与摘要标识，member 为包内位置，缺失成员表示等待补传。
packet_id 是投递标识，不是业务记录版本。record_id + task 指定现场对象，version/parents 给出来源父关系。
device_time 是设备报时，不作可信全序；任务签发名单在 assignment.py，演练设备均为虚构。
schema=v1 的 memo 对应 v2 的 note，其他未知字段须保留。迁移前后字段来源可同时展示。
deleted 标记删除状态；照片集合可随来源版本变化，撤回不能物理抹掉历史证据。
register_rows 消费 accepted、pending、conflict；accepted 要有 provenance。
样本 a、b 从共同父版本出发，分别改 condition 与 note；conflict 从同一父版本改 condition。
人工裁决应关联被裁决的来源版本及字段，不意味着以后同一字段的新修订也已获批准。
