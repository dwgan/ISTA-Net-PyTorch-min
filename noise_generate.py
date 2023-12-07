import torch

def noise_generate_e(e_snr, Phi, x):
    # calculation of measurement noise e
    Phix = x@Phi.T
    x_power = torch.sum(Phix**2) / torch.numel(Phix)
    e_power = x_power / 10**(e_snr / 10)
    e_std = torch.sqrt(e_power)
    e=e_std*torch.randn_like(Phix)

    return e

def noise_generate_E(E_snr, Phi, x):
    # calculation of Matrix noise E
    Phi_power = torch.sum(Phi.ravel()**2) / torch.numel(Phi)
    E_power = Phi_power / 10**(E_snr / 10)
    E_std = torch.sqrt(E_power)
    E=E_std*torch.randn_like(Phi)

    return E