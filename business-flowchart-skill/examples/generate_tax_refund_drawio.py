from xml.etree.ElementTree import Element, SubElement, ElementTree


def add_cell(root, cid, value="", style="", vertex=False, edge=False, parent="1", source=None, target=None, x=None, y=None, w=None, h=None):
    attrs = {"id": cid}
    if value:
        attrs["value"] = value
    if style:
        attrs["style"] = style
    attrs["parent"] = parent
    if vertex:
        attrs["vertex"] = "1"
    if edge:
        attrs["edge"] = "1"
    if source:
        attrs["source"] = source
    if target:
        attrs["target"] = target
    cell = SubElement(root, "mxCell", attrs)
    if vertex:
        SubElement(cell, "mxGeometry", {
            "x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"
        })
    if edge:
        SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    return cell


def graph_model():
    model = Element("mxGraphModel", {
        "dx": "1600", "dy": "900", "grid": "1", "gridSize": "10", "guides": "1",
        "tooltips": "1", "connect": "1", "arrows": "1", "fold": "1", "page": "1",
        "pageScale": "1", "pageWidth": "1920", "pageHeight": "1080", "math": "0", "shadow": "0"
    })
    root = SubElement(model, "root")
    SubElement(root, "mxCell", {"id": "0"})
    SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    return model, root


def main_page():
    model, root = graph_model()
    styles = {
        "title": "text;html=1;strokeColor=none;fillColor=none;fontSize=30;fontStyle=1;fontColor=#173B73;align=left;verticalAlign=middle;",
        "stage": "rounded=1;whiteSpace=wrap;html=1;fillColor=#EAF3FF;strokeColor=#BBD4FF;fontColor=#173B73;fontStyle=1;fontSize=16;",
        "start": "ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EAF3FF;strokeColor=#3B82F6;strokeWidth=2;fontColor=#082B60;fontStyle=1;",
        "end": "ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EAFBEF;strokeColor=#16A34A;strokeWidth=2;fontColor=#075E2B;fontStyle=1;",
        "node": "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4F8DFF;strokeWidth=2;fontColor=#082B60;fontStyle=1;spacing=8;",
        "decision": "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF7E8;strokeColor=#F59E0B;strokeWidth=2;fontColor=#7A3E00;fontStyle=1;spacing=8;",
        "green": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ECFDF3;strokeColor=#16A34A;strokeWidth=2;fontColor=#075E2B;fontStyle=1;spacing=8;",
        "lane": "text;html=1;strokeColor=none;fillColor=none;fontSize=16;fontStyle=1;fontColor=#5B6B84;align=right;verticalAlign=middle;",
        "edge": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#3B82F6;strokeWidth=3;endArrow=block;endFill=1;",
        "edge_yes": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#3B82F6;strokeWidth=3;endArrow=block;endFill=1;fontColor=#173B73;fontStyle=1;",
        "edge_green": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#16A34A;strokeWidth=3;endArrow=block;endFill=1;",
        "edge_exception": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#F97316;strokeWidth=2;dashed=1;endArrow=block;endFill=1;fontColor=#B45309;fontStyle=1;"
    }

    add_cell(root, "t1", "退税通业务流程图（主流程）", styles["title"], True, x=70, y=35, w=500, h=44)
    stages = ["01 行程建档", "02 消费购导", "03 退税申请", "04 物流交付", "05 离境核验", "06 到账监管"]
    xs = [160, 430, 700, 970, 1240, 1510]
    for i, (stage, x) in enumerate(zip(stages, xs), start=1):
        add_cell(root, f"s{i}", stage, styles["stage"], True, x=x, y=105, w=190, h=44)

    lanes = [("游客/用户", 210), ("平台/商户", 340), ("物流/机场", 470), ("代理/监管", 600)]
    for label, y in lanes:
        add_cell(root, f"lane_{y}", label, styles["lane"], True, x=25, y=y+5, w=110, h=40)

    nodes = [
        ("start", "开始", styles["start"], 80, 222, 70, 70),
        ("n1", "录入行程资料", styles["node"], 170, 210, 170, 58),
        ("d1", "资料是否完整？", styles["decision"], 185, 318, 140, 105),
        ("n2", "生成退税档案", styles["node"], 170, 505, 170, 58),
        ("n3", "推荐退税商户", styles["node"], 440, 210, 170, 58),
        ("n4", "到店消费购物", styles["node"], 440, 340, 170, 58),
        ("n5", "同步订单票据", styles["node"], 710, 340, 170, 58),
        ("d2", "材料是否齐全？", styles["decision"], 725, 470, 140, 105),
        ("n6", "提交退税申请", styles["node"], 710, 625, 170, 58),
        ("n7", "商户打包揽收", styles["node"], 980, 340, 170, 58),
        ("d3", "是否按时入库？", styles["decision"], 995, 470, 140, 105),
        ("n8", "推送领取提醒", styles["node"], 980, 625, 170, 58),
        ("n9", "生成机场路线", styles["node"], 1250, 210, 170, 58),
        ("d4", "核验是否通过？", styles["decision"], 1265, 340, 140, 105),
        ("n10", "确认商品交付", styles["node"], 1250, 505, 170, 58),
        ("n11", "退税代理处理", styles["node"], 1520, 340, 170, 58),
        ("d5", "到账是否成功？", styles["decision"], 1535, 470, 140, 105),
        ("n12", "到账通知归档", styles["green"], 1520, 625, 170, 58),
        ("end", "完成", styles["end"], 1740, 630, 70, 70),
    ]
    for cid, val, sty, x, y, w, h in nodes:
        add_cell(root, cid, val, sty, True, x=x, y=y, w=w, h=h)

    edges = [
        ("e1", "start", "n1", "", styles["edge"]),
        ("e2", "n1", "d1", "", styles["edge"]),
        ("e3", "d1", "n2", "是", styles["edge_yes"]),
        ("e4", "n2", "n3", "", styles["edge"]),
        ("e5", "n3", "n4", "", styles["edge"]),
        ("e6", "n4", "n5", "", styles["edge"]),
        ("e7", "n5", "d2", "", styles["edge"]),
        ("e8", "d2", "n6", "是", styles["edge_yes"]),
        ("e9", "n6", "n7", "", styles["edge"]),
        ("e10", "n7", "d3", "", styles["edge"]),
        ("e11", "d3", "n8", "是", styles["edge_yes"]),
        ("e12", "n8", "n9", "", styles["edge"]),
        ("e13", "n9", "d4", "", styles["edge"]),
        ("e14", "d4", "n10", "通过", styles["edge_yes"]),
        ("e15", "n10", "n11", "", styles["edge"]),
        ("e16", "n11", "d5", "", styles["edge"]),
        ("e17", "d5", "n12", "成功", styles["edge_green"]),
        ("e18", "n12", "end", "", styles["edge_green"]),
    ]
    for cid, src, tgt, label, sty in edges:
        add_cell(root, cid, label, sty, edge=True, source=src, target=tgt)

    exception_refs = [
        ("x1", "资料缺失补录", 350),
        ("x2", "票据材料补录核对", 620),
        ("x3", "超时预警协同处理", 890),
        ("x4", "现场人工复核处理", 1160),
        ("x5", "失败重试或人工介入", 1430),
    ]
    for cid, val, x in exception_refs:
        add_cell(root, cid, val, "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF7ED;strokeColor=#F97316;strokeWidth=2;dashed=1;fontColor=#9A3412;fontStyle=1;spacing=8;", True, x=x, y=790, w=190, h=58)

    ex_edges = [
        ("xe1", "d1", "x1", "否"),
        ("xe2", "d2", "x2", "否"),
        ("xe3", "d3", "x3", "否"),
        ("xe4", "d4", "x4", "不通过"),
        ("xe5", "d5", "x5", "失败"),
    ]
    for cid, src, tgt, label in ex_edges:
        add_cell(root, cid, label, styles["edge_exception"], edge=True, source=src, target=tgt)

    return model


def exception_page():
    model, root = graph_model()
    title = "text;html=1;strokeColor=none;fillColor=none;fontSize=30;fontStyle=1;fontColor=#173B73;align=left;verticalAlign=middle;"
    node = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#4F8DFF;strokeWidth=2;fontColor=#082B60;fontStyle=1;spacing=8;"
    dec = "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF7E8;strokeColor=#F59E0B;strokeWidth=2;fontColor=#7A3E00;fontStyle=1;spacing=8;"
    ex = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF7ED;strokeColor=#F97316;strokeWidth=2;dashed=1;fontColor=#9A3412;fontStyle=1;spacing=8;"
    green = "rounded=1;whiteSpace=wrap;html=1;fillColor=#ECFDF3;strokeColor=#16A34A;strokeWidth=2;fontColor=#075E2B;fontStyle=1;spacing=8;"
    edge = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#F97316;strokeWidth=2;dashed=1;endArrow=block;endFill=1;fontColor=#9A3412;fontStyle=1;"
    edge2 = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#3B82F6;strokeWidth=3;endArrow=block;endFill=1;fontColor=#173B73;fontStyle=1;"
    add_cell(root, "t2", "退税通业务流程图（异常处理）", title, True, x=70, y=35, w=560, h=44)
    items = [
        ("a1", "发现异常", ex, 120, 220, 150, 58),
        ("a2", "识别异常类型", dec, 340, 195, 140, 105),
        ("a3", "资料缺失", ex, 590, 120, 170, 58),
        ("a4", "票据异常", ex, 590, 235, 170, 58),
        ("a5", "物流超时", ex, 590, 350, 170, 58),
        ("a6", "核验失败", ex, 590, 465, 170, 58),
        ("a7", "用户补充资料", node, 850, 120, 170, 58),
        ("a8", "商户补录票据", node, 850, 235, 170, 58),
        ("a9", "物流协同处理", node, 850, 350, 170, 58),
        ("a10", "现场人工复核", node, 850, 465, 170, 58),
        ("a11", "是否处理完成？", dec, 1120, 285, 140, 105),
        ("a12", "回到对应主流程节点", green, 1370, 235, 190, 58),
        ("a13", "异常归档/人工结束", ex, 1370, 405, 190, 58),
    ]
    for cid, val, sty, x, y, w, h in items:
        add_cell(root, cid, val, sty, True, x=x, y=y, w=w, h=h)
    conns = [
        ("ae1", "a1", "a2", "", edge2),
        ("ae2", "a2", "a3", "资料", edge),
        ("ae3", "a2", "a4", "票据", edge),
        ("ae4", "a2", "a5", "物流", edge),
        ("ae5", "a2", "a6", "核验", edge),
        ("ae6", "a3", "a7", "", edge2),
        ("ae7", "a4", "a8", "", edge2),
        ("ae8", "a5", "a9", "", edge2),
        ("ae9", "a6", "a10", "", edge2),
        ("ae10", "a7", "a11", "", edge2),
        ("ae11", "a8", "a11", "", edge2),
        ("ae12", "a9", "a11", "", edge2),
        ("ae13", "a10", "a11", "", edge2),
        ("ae14", "a11", "a12", "是", edge2),
        ("ae15", "a11", "a13", "否", edge),
    ]
    for cid, src, tgt, label, sty in conns:
        add_cell(root, cid, label, sty, edge=True, source=src, target=tgt)
    return model


mxfile = Element("mxfile", {
    "host": "app.diagrams.net",
    "modified": "2026-06-18T00:00:00.000Z",
    "agent": "Codex",
    "version": "26.0.0",
    "type": "device"
})
diag1 = SubElement(mxfile, "diagram", {"id": "main", "name": "主流程"})
diag1.append(main_page())
diag2 = SubElement(mxfile, "diagram", {"id": "exception", "name": "异常处理"})
diag2.append(exception_page())

ElementTree(mxfile).write("/workspace/business-flowchart-skill/examples/tax-refund-clean.drawio", encoding="utf-8", xml_declaration=True)
