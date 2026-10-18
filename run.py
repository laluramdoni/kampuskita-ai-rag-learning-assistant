"""Entry point: python run.py"""
import uvicorn
if __name__=='__main__':
    print('\n✨ KampusKita AI is starting at http://127.0.0.1:8000\n')
    uvicorn.run('app.main:app',host='127.0.0.1',port=8000,reload=False)
