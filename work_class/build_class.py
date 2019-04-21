# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"碧蓝航线鞍山画板视频、图片生成工具", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"生成", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"生成" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_show = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap_show, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_slider_timeline = wx.Slider( self.m_panel1, wx.ID_ANY, 1, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_SELRANGE )
		bSizer2.Add( self.m_slider_timeline, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer6.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_gauge_line = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_line.SetValue( 0 )
		bSizer6.Add( self.m_gauge_line, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"加载视频", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"所有文件|*.*||*.flv||*.mp4||*.avi||*.mkv||*.wma||*.rmvb||*.mov", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer3.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_view_typeChoices = [ u"显示原始视频", u"显示效果视频" ]
		self.m_radioBox_view_type = wx.RadioBox( self.m_scrolledWindow1, wx.ID_ANY, u"显示类型", wx.DefaultPosition, wx.DefaultSize, m_radioBox_view_typeChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_view_type.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox_view_type, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline14 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"播放操作", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_reset = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button_reset, 0, wx.ALL, 5 )

		self.m_button_play_stop = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"播放/暂停", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button_play_stop, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline3 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"水平画板数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer14.Add( self.m_staticText121, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_wide = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl_wide, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText131 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"竖直画板数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer131.Add( self.m_staticText131, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_high = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_textCtrl_high, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer131, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"轮廓加粗", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer15.Add( self.m_staticText14, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_blur = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_textCtrl_blur, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer15, 0, wx.EXPAND, 5 )

		self.m_staticline141 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline141, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_cmp = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"显示比较视频", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox_cmp, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"左上角X坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer11.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_cmp_x = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl_cmp_x, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"左上角Y坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer12.Add( self.m_staticText11, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_cmp_y = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl_cmp_y, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"缩放", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer13.Add( self.m_staticText12, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_cmp_scale = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl_cmp_scale, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_staticline15 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"编码选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer3.Add( self.m_staticText13, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_use_in_code = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"使用输入编码", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox_use_in_code, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"XVID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.SetMaxLength( 4 )
		bSizer3.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline131 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline131, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"亮度/对比度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		bSizer3.Add( self.m_staticText111, 0, wx.ALL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"亮度" ), wx.VERTICAL )

		self.m_slider_light = wx.Slider( sbSizer1.GetStaticBox(), wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer1.Add( self.m_slider_light, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"对比度" ), wx.VERTICAL )

		self.m_slider_cmp = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer2.Add( self.m_slider_cmp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"饱和度" ), wx.VERTICAL )

		self.m_slider_full = wx.Slider( sbSizer3.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer3.Add( self.m_slider_full, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer3, 0, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer3 )
		self.m_scrolledWindow1.Layout()
		bSizer3.Fit( self.m_scrolledWindow1 )
		self.m_notebook1.AddPage( self.m_scrolledWindow1, u"视频", True )
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"加载图片（可多选）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_clean = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"清空列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_clean, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_load_img = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_load_img, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( bSizer7, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline7 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		m_listBox_input_imageChoices = []
		self.m_listBox_input_image = wx.ListBox( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,175 ), m_listBox_input_imageChoices, 0 )
		bSizer4.Add( self.m_listBox_input_image, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_staticline6 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		m_radioBox_view_type_imgChoices = [ u"显示原始视频", u"显示效果视频" ]
		self.m_radioBox_view_type_img = wx.RadioBox( self.m_scrolledWindow2, wx.ID_ANY, u"显示类型", wx.DefaultPosition, wx.DefaultSize, m_radioBox_view_type_imgChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_view_type_img.SetSelection( 1 )
		bSizer4.Add( self.m_radioBox_view_type_img, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1311 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1311, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1312 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1312, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer1311 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1311 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"竖直画板数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1311.Wrap( -1 )

		bSizer1311.Add( self.m_staticText1311, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_high_img = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1311.Add( self.m_textCtrl_high_img, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer1311, 0, wx.EXPAND, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1211 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"水平画板数量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )

		bSizer141.Add( self.m_staticText1211, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_wide_img = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_textCtrl_wide_img, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer141, 0, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText141 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"轮廓加粗", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		bSizer151.Add( self.m_staticText141, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl_blur_img = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.m_textCtrl_blur_img, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer151, 0, wx.EXPAND, 5 )

		self.m_staticline151 = wx.StaticLine( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline151, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText1111 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"亮度/对比度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )

		bSizer4.Add( self.m_staticText1111, 0, wx.ALL, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"亮度" ), wx.VERTICAL )

		self.m_slider_light1 = wx.Slider( sbSizer11.GetStaticBox(), wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer11.Add( self.m_slider_light1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer11, 1, wx.EXPAND, 5 )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"对比度" ), wx.VERTICAL )

		self.m_slider_cmp1 = wx.Slider( sbSizer21.GetStaticBox(), wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer21.Add( self.m_slider_cmp1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer21, 1, wx.EXPAND, 5 )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"饱和度" ), wx.VERTICAL )

		self.m_slider_full1 = wx.Slider( sbSizer31.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		sbSizer31.Add( self.m_slider_full1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer31, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer4 )
		self.m_scrolledWindow2.Layout()
		bSizer4.Fit( self.m_scrolledWindow2 )
		self.m_notebook1.AddPage( self.m_scrolledWindow2, u"图片", False )

		bSizer5.Add( self.m_notebook1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_info = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_info.Wrap( -1 )

		bSizer5.Add( self.m_staticText_info, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.build, id = self.m_menuItem1.GetId() )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.load_file )
		self.m_radioBox_view_type.Bind( wx.EVT_RADIOBOX, self.view_select )
		self.m_button_reset.Bind( wx.EVT_BUTTON, self.reset_play )
		self.m_button_play_stop.Bind( wx.EVT_BUTTON, self.play_pause )
		self.m_textCtrl_wide.Bind( wx.EVT_MOUSEWHEEL, self.wide_wheel )
		self.m_textCtrl_wide.Bind( wx.EVT_TEXT, self.set_wide )
		self.m_textCtrl_high.Bind( wx.EVT_MOUSEWHEEL, self.high_wheel )
		self.m_textCtrl_high.Bind( wx.EVT_TEXT, self.set_high )
		self.m_textCtrl_blur.Bind( wx.EVT_MOUSEWHEEL, self.blur_wheel )
		self.m_textCtrl_blur.Bind( wx.EVT_TEXT, self.set_blur )
		self.m_checkBox_cmp.Bind( wx.EVT_CHECKBOX, self.show_cmp )
		self.m_textCtrl_cmp_x.Bind( wx.EVT_MOUSEWHEEL, self.cmp_x_wheel )
		self.m_textCtrl_cmp_x.Bind( wx.EVT_TEXT, self.cmp_x_v )
		self.m_textCtrl_cmp_y.Bind( wx.EVT_MOUSEWHEEL, self.cmp_y_wheel )
		self.m_textCtrl_cmp_y.Bind( wx.EVT_TEXT, self.cmp_y_v )
		self.m_textCtrl_cmp_scale.Bind( wx.EVT_MOUSEWHEEL, self.cmp_sclae_wheel )
		self.m_textCtrl_cmp_scale.Bind( wx.EVT_TEXT, self.cmp_scale_v )
		self.m_checkBox_use_in_code.Bind( wx.EVT_CHECKBOX, self.use_in_code )
		self.m_textCtrl4.Bind( wx.EVT_TEXT, self.entry_coder )
		self.m_slider_light.Bind( wx.EVT_SCROLL_CHANGED, self.light_v )
		self.m_slider_cmp.Bind( wx.EVT_SCROLL_CHANGED, self.cmp_v )
		self.m_button_clean.Bind( wx.EVT_BUTTON, self.clean_list )
		self.m_button_load_img.Bind( wx.EVT_BUTTON, self.load_image )
		self.m_listBox_input_image.Bind( wx.EVT_LISTBOX, self.view_img )
		self.m_listBox_input_image.Bind( wx.EVT_LISTBOX_DCLICK, self.view_img )
		self.m_radioBox_view_type_img.Bind( wx.EVT_RADIOBOX, self.view_select )
		self.m_textCtrl_high_img.Bind( wx.EVT_MOUSEWHEEL, self.high_wheel )
		self.m_textCtrl_high_img.Bind( wx.EVT_TEXT, self.set_high )
		self.m_textCtrl_wide_img.Bind( wx.EVT_MOUSEWHEEL, self.wide_wheel )
		self.m_textCtrl_wide_img.Bind( wx.EVT_TEXT, self.set_wide )
		self.m_textCtrl_blur_img.Bind( wx.EVT_MOUSEWHEEL, self.blur_wheel )
		self.m_textCtrl_blur_img.Bind( wx.EVT_TEXT, self.set_blur )
		self.m_slider_light1.Bind( wx.EVT_SCROLL_CHANGED, self.light_v )
		self.m_slider_cmp1.Bind( wx.EVT_SCROLL_CHANGED, self.cmp_v )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def build( self, event ):
		event.Skip()

	def load_file( self, event ):
		event.Skip()

	def view_select( self, event ):
		event.Skip()

	def reset_play( self, event ):
		event.Skip()

	def play_pause( self, event ):
		event.Skip()

	def wide_wheel( self, event ):
		event.Skip()

	def set_wide( self, event ):
		event.Skip()

	def high_wheel( self, event ):
		event.Skip()

	def set_high( self, event ):
		event.Skip()

	def blur_wheel( self, event ):
		event.Skip()

	def set_blur( self, event ):
		event.Skip()

	def show_cmp( self, event ):
		event.Skip()

	def cmp_x_wheel( self, event ):
		event.Skip()

	def cmp_x_v( self, event ):
		event.Skip()

	def cmp_y_wheel( self, event ):
		event.Skip()

	def cmp_y_v( self, event ):
		event.Skip()

	def cmp_sclae_wheel( self, event ):
		event.Skip()

	def cmp_scale_v( self, event ):
		event.Skip()

	def use_in_code( self, event ):
		event.Skip()

	def entry_coder( self, event ):
		event.Skip()

	def light_v( self, event ):
		event.Skip()

	def cmp_v( self, event ):
		event.Skip()

	def clean_list( self, event ):
		event.Skip()

	def load_image( self, event ):
		event.Skip()

	def view_img( self, event ):
		event.Skip()












