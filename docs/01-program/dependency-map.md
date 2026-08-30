# Dependency / field map

Edges mean **usually useful before**, not "finish every page first."

```mermaid
flowchart TD
  subgraph Formal[Formal & inferential]
    Proof[Proof / specification]
    Calc[Calculus / vector calculus]
    LA[Linear algebra]
    ODE[Dynamics / ODEs]
    Prob[Probability]
    Causal[Statistics / causal inference]
    Num[Scientific computing]
    Opt[Optimization]
    Info[Information / signals]
    Ctrl[Control / estimation]
    Met[Metrology / experiments]
  end

  subgraph Physical[Physical & engineered]
    Mech[Mechanics / electromagnetism]
    Thermo[Thermo / statistical mechanics]
    QM[Quantum / condensed matter]
    Chem[Chemistry / materials]
    Elec[Electronics / embedded]
    Design[Mechanical design / fluids / structures]
  end

  subgraph Living[Living systems]
    Cell[Cell biology]
    Evo[Genetics / evolution / systems biology]
    Neuro[Neuroscience / physiology]
  end

  subgraph Scale[Scale & failure]
    Mfg[Manufacturing / operations]
    Safety[Safety / reliability / security]
  end

  Proof --> Calc
  Proof --> LA
  Calc --> ODE
  LA --> ODE
  LA --> Prob
  Prob --> Causal
  Calc --> Num
  LA --> Num
  ODE --> Num
  Prob --> Num
  Num --> Opt
  Prob --> Opt
  LA --> Info
  Prob --> Info
  ODE --> Ctrl
  Info --> Ctrl
  Opt --> Ctrl
  Prob --> Met

  Calc --> Mech
  ODE --> Mech
  Mech --> Thermo
  LA --> QM
  Prob --> QM
  Thermo --> Chem
  QM --> Chem
  Info --> Elec
  Ctrl --> Elec
  Mech --> Design
  Chem --> Design

  Thermo --> Cell
  Chem --> Cell
  Prob --> Cell
  Cell --> Evo
  Causal --> Evo
  Info --> Neuro
  Ctrl --> Neuro
  Cell --> Neuro

  Chem --> Mfg
  Elec --> Mfg
  Design --> Mfg
  Met --> Mfg
  Ctrl --> Safety
  Causal --> Safety
  Met --> Safety
  Mfg --> Safety

  Safety --> Tracks[7 specialization tracks]
  Mfg --> Tracks
  Evo --> Tracks
  Neuro --> Tracks
  QM --> Tracks
```

## Use

- **Forage:** enter at the nearest concept you do not own.
- **Sequence:** follow upstream arrows when a later topic feels like notation without intuition.
- **Contribute:** curriculum reordering should explain which dependencies have become cheaper, unnecessary, or teachable in parallel.
