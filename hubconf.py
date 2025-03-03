import torch
from utils.utils import Params
from backbone import HybridNetsBackbone


def hybridnets(pretrained=True, compound_coef=3, device=None):
    """Creates a HybridNets model

    Arguments:
        pretrained (bool): load pretrained weights into the model
        compound_coef (int): compound coefficient of efficientnet backbone
        device (str): 'cuda:0' or 'cpu'

    Returns:
        HybridNets model
    """
    params = Params(f'projects/bdd100k.yml')
    model = HybridNetsBackbone(num_classes=len(params.obj_list), compound_coef=compound_coef,
                               ratios=eval(params.anchors_ratios), scales=eval(params.anchors_scales),
                               seg_classes=len(params.seg_list))
    if pretrained and compound_coef == 3:
        weight_url = 'https://github.com/datvuthanh/HybridNets/releases/download/v1.1/hybridnets.pth'
        model.load_state_dict(torch.hub.load_state_dict_from_url(weight_url, map_location=device))
    model = model.to(device)
    return model


if __name__ == "__main__":
    model = hybridnets(device='cpu')
    img = torch.rand(1, 3, 384, 640)

    result = model(img)
    print(result)