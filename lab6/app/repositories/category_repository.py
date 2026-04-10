from ..models import Category

class CategoryRepository:
    def __init__(self, db):
        self.db = db

    def get_all_categories(self):
        return self.db.session.execute(self.db.select(Category)).scalars()
    
    def get_category_by_id(self, category_id):
        return self.db.session.execute(self.db.select(Category).filter_by(id=category_id)).scalar()