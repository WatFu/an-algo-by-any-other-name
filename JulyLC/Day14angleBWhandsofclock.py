class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_deg = (30*hour + 30*(minutes/60))%360
        m_deg = 6*minutes
        
        diff = min(abs(h_deg-m_deg), abs(m_deg-h_deg))
        
        if diff > 180:
            return 360-diff
        return diff
