export interface SVGIconProps {
  width: number;
  height: number;
  viewBox: string;
  path: string;
}

function SvgIcon({ width, height, viewBox, path }: SVGIconProps) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={width}
      height={height}
      viewBox={viewBox}
      fill="none"
    >
      <path d={path} fill="#860081" />
    </svg>
  );
}

export default SvgIcon;
