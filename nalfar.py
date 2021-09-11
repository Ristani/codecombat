def should_use_poison():
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy and 10 < hero.distanceTo(enemy) <= 30:
            return enemy


def attack_enemy(enemy):
    if hero.distanceTo(enemy) <= 15:
        hero.cast("drain-life", enemy)
    elif hero.distanceTo(enemy) <= 45:
        hero.attack(enemy)


while True:
    hero.moveXY(61, 60)
    if hero.canCast("raise-dead"):
        corpses = hero.findCorpses()
        if corpses.length > 5:
            hero.cast("raise-dead")
    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    foes = hero.findEnemies()
    warlocks = hero.findByType("warlock", foes)
    witches = hero.findByType("witch", foes)
    enemies = warlocks + witches
    enemy = hero.findNearest(enemies)
    if enemy:
        attack_enemy(enemy)
    else:
        fangriders = hero.findByType("fangrider", foes)
        throwers = hero.findByType("thrower", foes)
        shamans = hero.findByType("shaman", foes)
        enemies = fangriders+throwers+shamans
        enemy = hero.findNearest(enemies)
        if enemy:
            attack_enemy(enemy)
        else:
            enemy = hero.findNearestEnemy()
            if enemy:
                attack_enemy(enemy)
    should = should_use_poison()
    if hero.canCast("poison-cloud") and should:
        hero.cast("poison-cloud", should)
    friends = hero.findFriends()
    if friends:
        BFF = friends[0]
        for friend in friends:
            if friend.health > BFF.health:
                BFF = friend
        if BFF and hero.canCast("sacrifice"):
            hero.cast("sacrifice", BFF)
