

class DefaultConfig:

    five_stars_figures_root = 'imgs/five_stars_figures'
    four_stars_figures_root = 'imgs/four_stars_figures'
    five_stars_weapons_root = 'imgs/five_stars_weapons'
    four_stars_weapons_root = 'imgs/four_stars_weapons'
    three_stars_weapons_root = 'imgs/three_stars_weapons'

    up_five_stars_figures = '刻晴'
    up_four_stars_figures = '重云 香菱 行秋'

    def new_parse(self,**kwargs):
        for i,v in kwargs.items():
            setattr(self,i,v)