

class DefaultConfig:

    root = 'all_imgs'
    five_stars_figures_root = 'imgs/five_stars_figures'
    four_stars_figures_root = 'imgs/four_stars_figures'
    five_stars_weapons_root = 'imgs/five_stars_weapons'
    four_stars_weapons_root = 'imgs/four_stars_weapons'
    three_stars_weapons_root = 'imgs/three_stars_weapons'

    up_five_stars_figures = '胡桃'
    up_four_stars_figures = '班尼特 芭芭拉 凝光'

    def new_parse(self,**kwargs):
        for i,v in kwargs.items():
            setattr(self,i,v)