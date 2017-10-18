# The PEP 484 type hints stub file for the QtDeclarative module.
#
# Generated by SIP 4.19.3
#
# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt4.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt4 import QtNetwork
from PyQt4 import QtGui
from PyQt4 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Support for old-style signals and slots.
QT_SIGNAL = str
QT_SLOT = str


class QDeclarativeComponent(QtCore.QObject):

    class Status(int): ...
    Null = ... # type: 'QDeclarativeComponent.Status'
    Ready = ... # type: 'QDeclarativeComponent.Status'
    Loading = ... # type: 'QDeclarativeComponent.Status'
    Error = ... # type: 'QDeclarativeComponent.Status'

    @typing.overload
    def __init__(self, a0: 'QDeclarativeEngine', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeEngine', fileName: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeEngine', url: QtCore.QUrl, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def progressChanged(self, a0: float) -> None: ...
    def statusChanged(self, a0: 'QDeclarativeComponent.Status') -> None: ...
    def creationContext(self) -> 'QDeclarativeContext': ...
    def setData(self, a0: typing.Union[QtCore.QByteArray, bytes, bytearray], baseUrl: QtCore.QUrl) -> None: ...
    def loadUrl(self, url: QtCore.QUrl) -> None: ...
    def completeCreate(self) -> None: ...
    def beginCreate(self, a0: 'QDeclarativeContext') -> QtCore.QObject: ...
    def create(self, context: typing.Optional['QDeclarativeContext'] = ...) -> QtCore.QObject: ...
    def url(self) -> QtCore.QUrl: ...
    def progress(self) -> float: ...
    def errors(self) -> typing.Any: ...
    def isLoading(self) -> bool: ...
    def isError(self) -> bool: ...
    def isReady(self) -> bool: ...
    def isNull(self) -> bool: ...
    def status(self) -> 'QDeclarativeComponent.Status': ...


class QDeclarativeContext(QtCore.QObject):

    @typing.overload
    def __init__(self, engine: 'QDeclarativeEngine', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, context: 'QDeclarativeContext', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def baseUrl(self) -> QtCore.QUrl: ...
    def setBaseUrl(self, a0: QtCore.QUrl) -> None: ...
    def resolvedUrl(self, a0: QtCore.QUrl) -> QtCore.QUrl: ...
    @typing.overload
    def setContextProperty(self, a0: str, a1: QtCore.QObject) -> None: ...
    @typing.overload
    def setContextProperty(self, a0: str, a1: typing.Any) -> None: ...
    def contextProperty(self, a0: str) -> typing.Any: ...
    def setContextObject(self, a0: QtCore.QObject) -> None: ...
    def contextObject(self) -> QtCore.QObject: ...
    def parentContext(self) -> 'QDeclarativeContext': ...
    def engine(self) -> 'QDeclarativeEngine': ...
    def isValid(self) -> bool: ...


class QDeclarativeEngine(QtCore.QObject):

    class ObjectOwnership(int): ...
    CppOwnership = ... # type: 'QDeclarativeEngine.ObjectOwnership'
    JavaScriptOwnership = ... # type: 'QDeclarativeEngine.ObjectOwnership'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def warnings(self, warnings: typing.Sequence['QDeclarativeError']) -> None: ...
    def quit(self) -> None: ...
    @staticmethod
    def objectOwnership(a0: QtCore.QObject) -> 'QDeclarativeEngine.ObjectOwnership': ...
    @staticmethod
    def setObjectOwnership(a0: QtCore.QObject, a1: 'QDeclarativeEngine.ObjectOwnership') -> None: ...
    @staticmethod
    def setContextForObject(a0: QtCore.QObject, a1: QDeclarativeContext) -> None: ...
    @staticmethod
    def contextForObject(a0: QtCore.QObject) -> QDeclarativeContext: ...
    def setOutputWarningsToStandardError(self, a0: bool) -> None: ...
    def outputWarningsToStandardError(self) -> bool: ...
    def setBaseUrl(self, a0: QtCore.QUrl) -> None: ...
    def baseUrl(self) -> QtCore.QUrl: ...
    def offlineStoragePath(self) -> str: ...
    def setOfflineStoragePath(self, dir: str) -> None: ...
    def removeImageProvider(self, id: str) -> None: ...
    def imageProvider(self, id: str) -> 'QDeclarativeImageProvider': ...
    def addImageProvider(self, id: str, a1: 'QDeclarativeImageProvider') -> None: ...
    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def networkAccessManagerFactory(self) -> 'QDeclarativeNetworkAccessManagerFactory': ...
    def setNetworkAccessManagerFactory(self, a0: 'QDeclarativeNetworkAccessManagerFactory') -> None: ...
    def importPlugin(self, filePath: str, uri: str) -> typing.Tuple[bool, str]: ...
    def addPluginPath(self, dir: str) -> None: ...
    def setPluginPathList(self, paths: typing.Sequence[str]) -> None: ...
    def pluginPathList(self) -> typing.List[str]: ...
    def addImportPath(self, dir: str) -> None: ...
    def setImportPathList(self, paths: typing.Sequence[str]) -> None: ...
    def importPathList(self) -> typing.List[str]: ...
    def clearComponentCache(self) -> None: ...
    def rootContext(self) -> QDeclarativeContext: ...


class QDeclarativeError(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeError') -> None: ...

    def toString(self) -> str: ...
    def setColumn(self, a0: int) -> None: ...
    def column(self) -> int: ...
    def setLine(self, a0: int) -> None: ...
    def line(self) -> int: ...
    def setDescription(self, a0: str) -> None: ...
    def description(self) -> str: ...
    def setUrl(self, a0: QtCore.QUrl) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def isValid(self) -> bool: ...


class QDeclarativeExpression(QtCore.QObject):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QDeclarativeContext, a1: QtCore.QObject, a2: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def valueChanged(self) -> None: ...
    def evaluate(self) -> typing.Tuple[typing.Any, bool]: ...
    def error(self) -> QDeclarativeError: ...
    def clearError(self) -> None: ...
    def hasError(self) -> bool: ...
    def scopeObject(self) -> QtCore.QObject: ...
    def setSourceLocation(self, fileName: str, line: int) -> None: ...
    def lineNumber(self) -> int: ...
    def sourceFile(self) -> str: ...
    def setNotifyOnValueChanged(self, a0: bool) -> None: ...
    def notifyOnValueChanged(self) -> bool: ...
    def setExpression(self, a0: str) -> None: ...
    def expression(self) -> str: ...
    def context(self) -> QDeclarativeContext: ...
    def engine(self) -> QDeclarativeEngine: ...


class QDeclarativeExtensionPlugin(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def initializeEngine(self, engine: QDeclarativeEngine, uri: str) -> None: ...
    def registerTypes(self, uri: str) -> None: ...


class QDeclarativeImageProvider(sip.simplewrapper):

    class ImageType(int): ...
    Image = ... # type: 'QDeclarativeImageProvider.ImageType'
    Pixmap = ... # type: 'QDeclarativeImageProvider.ImageType'

    @typing.overload
    def __init__(self, type: 'QDeclarativeImageProvider.ImageType') -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeImageProvider') -> None: ...

    def requestPixmap(self, id: str, size: QtCore.QSize, requestedSize: QtCore.QSize) -> QtGui.QPixmap: ...
    def requestImage(self, id: str, size: QtCore.QSize, requestedSize: QtCore.QSize) -> QtGui.QImage: ...
    def imageType(self) -> 'QDeclarativeImageProvider.ImageType': ...


class QDeclarativeParserStatus(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeParserStatus') -> None: ...

    def componentComplete(self) -> None: ...
    def classBegin(self) -> None: ...


class QDeclarativeItem(QtGui.QGraphicsObject, QDeclarativeParserStatus):

    class TransformOrigin(int): ...
    TopLeft = ... # type: 'QDeclarativeItem.TransformOrigin'
    Top = ... # type: 'QDeclarativeItem.TransformOrigin'
    TopRight = ... # type: 'QDeclarativeItem.TransformOrigin'
    Left = ... # type: 'QDeclarativeItem.TransformOrigin'
    Center = ... # type: 'QDeclarativeItem.TransformOrigin'
    Right = ... # type: 'QDeclarativeItem.TransformOrigin'
    BottomLeft = ... # type: 'QDeclarativeItem.TransformOrigin'
    Bottom = ... # type: 'QDeclarativeItem.TransformOrigin'
    BottomRight = ... # type: 'QDeclarativeItem.TransformOrigin'

    def __init__(self, parent: typing.Optional['QDeclarativeItem'] = ...) -> None: ...

    def geometryChanged(self, newGeometry: QtCore.QRectF, oldGeometry: QtCore.QRectF) -> None: ...
    def inputMethodQuery(self, query: QtCore.Qt.InputMethodQuery) -> typing.Any: ...
    def inputMethodEvent(self, a0: QtGui.QInputMethodEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def componentComplete(self) -> None: ...
    def classBegin(self) -> None: ...
    def heightValid(self) -> bool: ...
    def setImplicitHeight(self, a0: float) -> None: ...
    def widthValid(self) -> bool: ...
    def setImplicitWidth(self, a0: float) -> None: ...
    def itemChange(self, a0: QtGui.QGraphicsItem.GraphicsItemChange, a1: typing.Any) -> typing.Any: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def sceneEvent(self, a0: QtCore.QEvent) -> bool: ...
    def isComponentComplete(self) -> bool: ...
    def setKeepMouseGrab(self, a0: bool) -> None: ...
    def keepMouseGrab(self) -> bool: ...
    def hasFocus(self) -> bool: ...
    def paint(self, a0: QtGui.QPainter, a1: QtGui.QStyleOptionGraphicsItem, a2: QtGui.QWidget) -> None: ...
    def boundingRect(self) -> QtCore.QRectF: ...
    def setSmooth(self, a0: bool) -> None: ...
    def smooth(self) -> bool: ...
    def setTransformOrigin(self, a0: 'QDeclarativeItem.TransformOrigin') -> None: ...
    def transformOrigin(self) -> 'QDeclarativeItem.TransformOrigin': ...
    def implicitHeight(self) -> float: ...
    def setHeight(self, a0: float) -> None: ...
    def implicitWidth(self) -> float: ...
    def setWidth(self, a0: float) -> None: ...
    def setBaselineOffset(self, a0: float) -> None: ...
    def baselineOffset(self) -> float: ...
    def setClip(self, a0: bool) -> None: ...
    def clip(self) -> bool: ...
    def childrenRect(self) -> QtCore.QRectF: ...
    def setParentItem(self, parent: 'QDeclarativeItem') -> None: ...
    def parentItem(self) -> 'QDeclarativeItem': ...


class QDeclarativeListReference(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, property: str, engine: typing.Optional[QDeclarativeEngine] = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeListReference') -> None: ...

    def count(self) -> int: ...
    def clear(self) -> bool: ...
    def at(self, a0: int) -> QtCore.QObject: ...
    def append(self, a0: QtCore.QObject) -> bool: ...
    def canCount(self) -> bool: ...
    def canClear(self) -> bool: ...
    def canAt(self) -> bool: ...
    def canAppend(self) -> bool: ...
    def listElementType(self) -> QtCore.QMetaObject: ...
    def object(self) -> QtCore.QObject: ...
    def isValid(self) -> bool: ...


class QDeclarativeNetworkAccessManagerFactory(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeNetworkAccessManagerFactory') -> None: ...

    def create(self, parent: QtCore.QObject) -> QtNetwork.QNetworkAccessManager: ...


class QDeclarativeProperty(sip.simplewrapper):

    class Type(int): ...
    Invalid = ... # type: 'QDeclarativeProperty.Type'
    Property = ... # type: 'QDeclarativeProperty.Type'
    SignalProperty = ... # type: 'QDeclarativeProperty.Type'

    class PropertyTypeCategory(int): ...
    InvalidCategory = ... # type: 'QDeclarativeProperty.PropertyTypeCategory'
    List = ... # type: 'QDeclarativeProperty.PropertyTypeCategory'
    Object = ... # type: 'QDeclarativeProperty.PropertyTypeCategory'
    Normal = ... # type: 'QDeclarativeProperty.PropertyTypeCategory'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: QDeclarativeContext) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: QDeclarativeEngine) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str, a2: QDeclarativeContext) -> None: ...
    @typing.overload
    def __init__(self, a0: QtCore.QObject, a1: str, a2: QDeclarativeEngine) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeProperty') -> None: ...

    def __hash__(self) -> int: ...
    def method(self) -> QtCore.QMetaMethod: ...
    def property(self) -> QtCore.QMetaProperty: ...
    def index(self) -> int: ...
    def object(self) -> QtCore.QObject: ...
    def isResettable(self) -> bool: ...
    def isDesignable(self) -> bool: ...
    def isWritable(self) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, dest: QtCore.QObject, slot: QT_SLOT) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def connectNotifySignal(self, dest: QtCore.QObject, method: int) -> bool: ...
    def needsNotifySignal(self) -> bool: ...
    def hasNotifySignal(self) -> bool: ...
    def reset(self) -> bool: ...
    @typing.overload
    def write(self, a0: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any, a3: QDeclarativeContext) -> bool: ...
    @typing.overload
    @staticmethod
    def write(a0: QtCore.QObject, a1: str, a2: typing.Any, a3: QDeclarativeEngine) -> bool: ...
    @typing.overload
    def read(self) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str, a2: QDeclarativeContext) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def read(a0: QtCore.QObject, a1: str, a2: QDeclarativeEngine) -> typing.Any: ...
    def name(self) -> str: ...
    def propertyTypeName(self) -> str: ...
    def propertyTypeCategory(self) -> 'QDeclarativeProperty.PropertyTypeCategory': ...
    def propertyType(self) -> int: ...
    def isSignalProperty(self) -> bool: ...
    def isProperty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def type(self) -> 'QDeclarativeProperty.Type': ...


class QDeclarativePropertyMap(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def valueChanged(self, key: str, value: typing.Any) -> None: ...
    def __getitem__(self, key: str) -> typing.Any: ...
    def contains(self, key: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def keys(self) -> typing.List[str]: ...
    def clear(self, key: str) -> None: ...
    def insert(self, key: str, value: typing.Any) -> None: ...
    def value(self, key: str) -> typing.Any: ...


class QDeclarativePropertyValueSource(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativePropertyValueSource') -> None: ...

    def setTarget(self, a0: QDeclarativeProperty) -> None: ...


class QDeclarativeScriptString(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDeclarativeScriptString') -> None: ...

    def setScript(self, a0: str) -> None: ...
    def script(self) -> str: ...
    def setScopeObject(self, a0: QtCore.QObject) -> None: ...
    def scopeObject(self) -> QtCore.QObject: ...
    def setContext(self, a0: QDeclarativeContext) -> None: ...
    def context(self) -> QDeclarativeContext: ...


class QDeclarativeView(QtGui.QGraphicsView):

    class Status(int): ...
    Null = ... # type: 'QDeclarativeView.Status'
    Ready = ... # type: 'QDeclarativeView.Status'
    Loading = ... # type: 'QDeclarativeView.Status'
    Error = ... # type: 'QDeclarativeView.Status'

    class ResizeMode(int): ...
    SizeViewToRootObject = ... # type: 'QDeclarativeView.ResizeMode'
    SizeRootObjectToView = ... # type: 'QDeclarativeView.ResizeMode'

    @typing.overload
    def __init__(self, parent: typing.Optional[QtGui.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, source: QtCore.QUrl, parent: typing.Optional[QtGui.QWidget] = ...) -> None: ...

    def eventFilter(self, watched: QtCore.QObject, e: QtCore.QEvent) -> bool: ...
    def timerEvent(self, a0: QtCore.QTimerEvent) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None: ...
    def statusChanged(self, a0: 'QDeclarativeView.Status') -> None: ...
    def sceneResized(self, size: QtCore.QSize) -> None: ...
    def initialSize(self) -> QtCore.QSize: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def errors(self) -> typing.List[QDeclarativeError]: ...
    def status(self) -> 'QDeclarativeView.Status': ...
    def setResizeMode(self, a0: 'QDeclarativeView.ResizeMode') -> None: ...
    def resizeMode(self) -> 'QDeclarativeView.ResizeMode': ...
    def rootObject(self) -> QtGui.QGraphicsObject: ...
    def rootContext(self) -> QDeclarativeContext: ...
    def engine(self) -> QDeclarativeEngine: ...
    def setSource(self, a0: QtCore.QUrl) -> None: ...
    def source(self) -> QtCore.QUrl: ...


class QPyDeclarativePropertyValueSource(QtCore.QObject, QDeclarativePropertyValueSource):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
