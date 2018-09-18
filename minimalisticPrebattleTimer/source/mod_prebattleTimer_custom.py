import BigWorld
from gui.Scaleform.daapi.view.battle.shared.battle_timers import PreBattleTimer

MAIN_BG_ALPHA = 0.2
TASK_TITLE_SCALE = 0.9
SHOW_FLAG = False

TASK_TITLE_SCALE_FACTOR = (2.0 - TASK_TITLE_SCALE) * 1.1

def _delayedAccessor(prbInstance):
    emptyObj = 'emptyValue'
    qpSprite = emptyObj
    fObj = prbInstance.flashObject
    for idx in xrange(fObj.numChildren):
        obj = fObj.getChildAt(idx)
        if obj.name == 'qpInfoFlagContainer':
            qpSprite = next(iter(filter(lambda k: 'instance' in k, obj.children.keys())), emptyObj)
            if qpSprite != emptyObj:
                break
    qpSub = getattr(fObj.qpInfoFlagContainer, qpSprite, None)
    if qpSub:
        qpSub.flagBg.visible = SHOW_FLAG
        qpSub.taskIcoContainer.visible = SHOW_FLAG
        qpSub.taskIndex.visible = SHOW_FLAG
        qpSub.questFlagBgShadow.visible = SHOW_FLAG
        qpSub.taskTitle.scaleX = qpSub.taskTitle.scaleY = TASK_TITLE_SCALE
        qpSub.taskTitle.y = qpSub.flagBg.y - (qpSub.taskTitle.height * TASK_TITLE_SCALE_FACTOR)
    else:
        BigWorld.callback(0.1, lambda: _delayedAccessor(prbInstance))

def new_prbTimer_populate(self):
    old_prbTimer_populate(self)
    fObj = self.flashObject
    fObj.timer.scaleX = fObj.timer.scaleY = 0.63
    fObj.timer.scaleY = 0.63
    fObj.background.alpha = MAIN_BG_ALPHA
    fObj.message.y = fObj.timer.y + fObj.timer.height - 15
    fObj.win.y = fObj.message.y + fObj.message.height + 5
    BigWorld.callback(0.05, lambda: _delayedAccessor(self))

old_prbTimer_populate = PreBattleTimer._populate
PreBattleTimer._populate = new_prbTimer_populate

print '[NOTE] package loaded: prebattleTimer_custom v.1.0 by PolarFox (WoT 1.1)'