import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt

def set_lr(epoch,optimizer,lr_att):
    lr = lr_att
    if epoch <= 70 and epoch > 40:
        lr = lr_att * 0.1
    if epoch > 70:
        lr = lr_att*0.01
    for g in optimizer.param_groups:
        g['lr'] = lr * g.get('lr_mult', 1)
    #  print('decrease learning rate='+str(lr))



def adjust_lr(epoch,optimizer,lr_reid):
    lr = lr_reid
    if epoch <= 10 and epoch >= 1:
        lr = lr_reid + ((0.00035 - 0.000035) / 10.0) * epoch
    if epoch <= 40 and epoch > 10:
        lr = lr_reid * 10.0
    if epoch <= 70 and epoch > 40:
        lr = lr_reid
    if epoch <= 120 and epoch > 70:
        lr = lr_reid / 10.0
    #  print('warmup learning rate='+str(lr))

    for g in optimizer.param_groups:
        g['lr'] = lr * g.get('lr_mult', 1)



def to_scalar(vt):
  """Transform a length-1 pytorch Variable or Tensor to scalar.
  Suppose tx is a torch Tensor with shape tx.size() = torch.Size([1]),
  then npx = tx.cpu().numpy() has shape (1,), not 1."""
  if isinstance(vt, Variable):
    return vt.data.cpu().numpy().flatten()[0]
  if torch.is_tensor(vt):
    return vt.cpu().numpy().flatten()[0]
  raise TypeError('Input should be a variable or tensor')
 
def visualize(finalDf,ylabel,xlabel,title,fname):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_title(title, fontsize=20)
    #
    targets = [1, 2]
    colors = ['r', 'g']
    for target, color in zip(targets, colors):
        if color=='r':
             indicesToKeep = finalDf[0] == target
             ax.scatter(finalDf.loc[indicesToKeep, 1]
                        , finalDf.loc[indicesToKeep, 2]
                        , c=color
                        , s=5)
        else:
             indicesToKeep = finalDf[0] == target
             ax.scatter(finalDf.loc[indicesToKeep, 1]
                        , finalDf.loc[indicesToKeep, 2]
                        , c=color
                        , s=5)



    ax.legend(targets)
    ax.grid()
    plt.savefig(fname)
